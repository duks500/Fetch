from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from core.models import Client, Spend, PointBalance, SpendFinal
from . import serializers

def SpendFinalGenerator(current_transaction_GET, current_transaction, final_total_point_remove):
    """An helper function to calculate the total spend from each payer"""
    if current_transaction != 0:
        """No more transcations in the queue"""
        if SpendFinal.objects.filter(payer=current_transaction_GET.payer).exists():
            """Add to an existing payer"""
            spendfinal = SpendFinal.objects.get(payer=current_transaction_GET.payer)
            spendfinal.points = (spendfinal.points - current_transaction)
            spendfinal.save()
        else:
            """Create a new payer in the system"""
            SpendFinal.objects.create(
                payer=current_transaction_GET.payer,
                points= (-1 * current_transaction)
            )
    else:
        """More transactions in the queue"""
        if SpendFinal.objects.filter(payer=current_transaction_GET.payer).exists():
            """Add to an existing payer"""
            spendfinal = SpendFinal.objects.get(payer=current_transaction_GET.payer)
            spendfinal.points = (spendfinal.points - final_total_point_remove)
            spendfinal.save()
        else:
            """Create a new payer in the system"""
            SpendFinal.objects.create(
                payer=current_transaction_GET.payer,
                points= (-1 * final_total_point_remove)
            )



class AddTransaction(viewsets.ModelViewSet):
    """Manage add transaction in the database"""
    serializer_class = serializers.ClientPOST
    queryset = Client.objects.all()
    renderer_classes = [JSONRenderer,]

    def list(self, request, format=None):
        """GET"""
        queryset = Client.objects.all()
        serializer = serializers.ClientGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if PointBalance.objects.filter(payer=serializer.data['payer']).exists():
            """Add to an existing payer"""
            points = PointBalance.objects.get(payer=serializer.data['payer'])
            new_total_points = int(serializer.data['points']) + points.points

            PointBalance.objects.filter(payer=serializer.data['payer']).update(
                points=new_total_points,
            )
        else:
            """Create a new payer"""
            PointBalance.objects.create(
                payer=serializer.data['payer'],
                points=serializer.data['points']
           )
        return Response(serializer.data)


class SpednPoints(viewsets.ModelViewSet):
    """Manage spedn points in the database"""
    serializer_class = serializers.SpendPOST
    queryset = Spend.objects.all()
    renderer_classes = [JSONRenderer,]

    def list(self, request, format=None):
        """GET"""
        queryset = Spend.objects.all()
        serializer = serializers.SpendGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""
        # Delete the old data
        SpendFinal.objects.all().delete()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        total_points = serializer.data['points']

        try:
            """Check for errors"""
            # While condition
            equal_zero = True
            while equal_zero == True:
                """a loop to check every transaction separately"""
                #Get current transaction state
                current_transaction = Client.objects.filter().order_by('timestamp').first()
                current_transaction_GET = Client.objects.get(
                    payer=current_transaction.payer,
                    timestamp=current_transaction.timestamp
                )

                final_total_point_remove = current_transaction.points - total_points
                # Current final balance based on the payer
                current_final_balance = PointBalance.objects.get(payer=current_transaction.payer)

                if (total_points - current_transaction.points) < 0:
                    """This state is the last one that the bot need to check"""
                    # Updating the tables
                    PointBalance.objects.filter(payer=current_transaction.payer).update(
                        points=(current_final_balance.points - total_points)
                    )
                    Client.objects.filter(id=current_transaction.id).update(
                        points=(current_transaction.points - total_points)
                    )
                    SpendFinalGenerator(current_transaction_GET, 0, total_points)
                    equal_zero = False

                else:
                    """Check this state and than loop again to check the next one in line"""
                    # Updating the tables
                    total_points = total_points - current_transaction.points
                    PointBalance.objects.filter(payer=current_transaction.payer).update(
                        points=(current_final_balance.points - current_transaction.points)
                    )
                    SpendFinalGenerator(current_transaction_GET, current_transaction.points, 0)
                    # Delete this state
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
    renderer_classes = [JSONRenderer,]

    def list(self, request, format=None):
        """GET"""
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
    renderer_classes = [JSONRenderer,]

    def list(self, request, format=None):
        """GET"""
        queryset = SpendFinal.objects.all()
        serializer = serializers.SpendFinalGET(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """POST"""
        pass