from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from core.models import Client, Spend, PointBalance, SpendFinal
from . import serializers

def SpendFinalGenerator(current_transaction_GET, current_transaction, final_total_point_remove):
    """An helper function to calulate the total spend from each payer"""
    if current_transaction != 0:
        """Not last part"""
        if SpendFinal.objects.filter(payer=current_transaction_GET.payer).exists():
            """Add to an existing payer"""
            spendfinal = SpendFinal.objects.get(payer=current_transaction_GET.payer)
            spendfinal.points = (spendfinal.points - current_transaction)
            spendfinal.save()
        else:
            """New payer"""
            SpendFinal.objects.create(
                payer=current_transaction_GET.payer,
                points= (-1 * current_transaction)
            )
    else:
        """Last"""
        if SpendFinal.objects.filter(payer=current_transaction_GET.payer).exists():
            """Add to an existing payer"""
            spendfinal = SpendFinal.objects.get(payer=current_transaction_GET.payer)
            spendfinal.points = (spendfinal.points - final_total_point_remove)
            spendfinal.save()
        else:
            """New payer"""
            SpendFinal.objects.create(
                payer=current_transaction_GET.payer,
                points= (-1 * final_total_point_remove)
            )



class AddTransaction(viewsets.ModelViewSet):
    """Manage add transaction in the database"""
    serializer_class = serializers.ClientPOST
    queryset = Client.objects.all()
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]

    def list(self, request, format=None):
        """GET"""
        print('get')
        queryset = Client.objects.all()
        serializer = serializers.ClientGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if PointBalance.objects.filter(payer=serializer.data['payer']).exists():
            """If yes - exissting payer"""
            points = PointBalance.objects.get(payer=serializer.data['payer'])
            new_total_points = int(serializer.data['points']) + points.points

            PointBalance.objects.filter(payer=serializer.data['payer']).update(
                points=new_total_points,
            )
        else:
            """No payer, add a new one"""
            PointBalance.objects.create(
                payer=serializer.data['payer'],
                points=serializer.data['points']
           )
        return Response(serializer.data)


class SpednPoints(viewsets.ModelViewSet):
    """Manage spedn points in the database"""
    serializer_class = serializers.SpendPOST
    queryset = Spend.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request, format=None):
        """GET"""
        print('get')
        queryset = Spend.objects.all()
        serializer = serializers.SpendGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""

        SpendFinal.objects.all().delete()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        total_points = serializer.data['points']

        try:
            """Check for errors"""
            print('total points')
            print(total_points)


            equal_zero = True
            while equal_zero == True:
                """"""
                print('new while----------')
                current_transaction = Client.objects.filter().order_by('timestamp').first()
                current_transaction_GET = Client.objects.get(
                    payer=current_transaction.payer,
                    timestamp=current_transaction.timestamp
                )
                final_total_point_remove = current_transaction.points - total_points
                print('current_transaction.points - total_points')
                print(final_total_point_remove)
                print('current_transaction.points')
                print(current_transaction.points)
                print(total_points - current_transaction.points)
                current_final_balance = PointBalance.objects.get(payer=current_transaction.payer)
                print('current_transaction')
                print(current_transaction)
                print('current_transaction.points')
                print(current_transaction.points)
                print('current_transaction.payer')
                print(current_transaction.payer)
                print('total_points - current_transaction.points')
                print(total_points - current_transaction.points)

                if (total_points - current_transaction.points) < 0:
                    """No more moves possible"""
                    print('No more moves possble')
                    PointBalance.objects.filter(payer=current_transaction.payer).update(
                        points=(current_final_balance.points - total_points)
                    )
                    Client.objects.filter(id=current_transaction.id).update(
                        points=(current_transaction.points - total_points)
                    )
                    print('current_final_balance.points')
                    print(current_final_balance.points)
                    print(current_transaction_GET.points)
                    SpendFinalGenerator(current_transaction_GET, 0, total_points)
                    equal_zero = False

                else:
                    """Recursive"""
                    print('recursive')
                    total_points = total_points - current_transaction.points
                    print('new total points')
                    print(total_points)
                    PointBalance.objects.filter(payer=current_transaction.payer).update(
                        points=(current_final_balance.points - current_transaction.points)
                    )
                    print('current_final_balance.points')
                    # print(current_final_balance.points)
                    print(current_transaction_GET.points)
                    SpendFinalGenerator(current_transaction_GET, current_transaction.points, 0)
                    current_transaction.delete()

            queryset = SpendFinal.objects.all()
            serializer = serializers.SpendFinalGET(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            print(e)
            return Response(serializer.data)


class PointFinalBalance(viewsets.ModelViewSet):
    """Manage spedn points in the database"""
    serializer_class = serializers.PointBalancePOST
    queryset = PointBalance.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request, format=None):
        """GET"""
        print('get')
        queryset = PointBalance.objects.all()
        serializer = serializers.PointBalanceGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""
        pass


class SpendFinalBalance(viewsets.ModelViewSet):
    """Manage spedn points in the database"""
    serializer_class = serializers.SpendFinalPOST
    queryset = SpendFinal.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request, format=None):
        """GET"""
        print('get')
        queryset = SpendFinal.objects.all()
        serializer = serializers.SpendFinalGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""
        pass