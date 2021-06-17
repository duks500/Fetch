from rest_framework import serializers

from core.models import Client, Spend, PointBalance, SpendFinal


class ClientGET(serializers.ModelSerializer):
    """Serialie Client GET"""
    class Meta:
        model = Client
        fields = ('payer', 'points', 'timestamp',)


class ClientPOST(serializers.ModelSerializer):
    """Serialie Client POST"""
    class Meta:
        model = Client
        fields = '__all__'


class SpendGET(serializers.ModelSerializer):
    """Serialie Spend GET"""
    class Meta:
        model = Spend
        fields = ('points', 'timestamp',)


class SpendPOST(serializers.ModelSerializer):
    """Serialie Spend POST"""
    class Meta:
        model = Spend
        fields = ('points',)


class PointBalanceGET(serializers.ModelSerializer):
    """Serialie PointBalance GET"""
    class Meta:
        model = PointBalance
        fields = ('payer', 'points',)


class PointBalancePOST(serializers.ModelSerializer):
    """Serialie PointBalance POST"""
    class Meta:
        model = PointBalance
        fields = ('payer', 'points',)


class SpendFinalGET(serializers.ModelSerializer):
    """Serialie SpendFinal GET"""
    class Meta:
        model = SpendFinal
        fields = ('payer', 'points',)


class SpendFinalPOST(serializers.ModelSerializer):
    """Serialie SpendFinal POST"""
    class Meta:
        model = SpendFinal
        fields = ('payer', 'points',)