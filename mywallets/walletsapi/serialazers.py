from rest_framework import serializers
from .models import Wallet, Transactions


class WalletSerialazer(serializers.Serializer):
    name = serializers.CharField(max_length=8, read_only=True)
    type = serializers.CharField(max_length=11)
    currency = serializers.CharField(max_length=3)
    balance = serializers.DecimalField(max_digits=11, decimal_places=2, read_only=True)
    user_id = serializers.CharField(read_only=True)
    created_on = serializers.DateTimeField(read_only=True, format="%Y.%m.%d %H:%M:%S")
    modefied_on = serializers.DateTimeField(read_only=True, format="%Y.%m.%d %H:%M:%S")

class TransactionSerialazer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender = serializers.CharField(max_length=8)
    receiver = serializers.CharField(max_length=8)
    transfer_amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    commision = serializers.DecimalField(read_only=True, max_digits=11, decimal_places=2)
    status = serializers.CharField(read_only=True, max_length=6)
    timestamp = serializers.DateTimeField(read_only=True, format="%Y.%m.%d %H:%M:%S")