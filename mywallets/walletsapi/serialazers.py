from rest_framework import serializers
from .models import Wallet, Transactions, Currency


class WalletSerialazer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=8, read_only=True)
    type = serializers.ChoiceField(choices=Wallet.CARD_TYPE)
    currency = serializers.ChoiceField(choices=Currency.choices)
    balance = serializers.DecimalField(max_digits=11, decimal_places=2, read_only=True)
    created_on = serializers.DateTimeField(read_only=True, format="%Y.%m.%d %H:%M:%S")
    modefied_on = serializers.DateTimeField(read_only=True, format="%Y.%m.%d %H:%M:%S")

class TransactionSerialazer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender = serializers.CharField(max_length=8)
    receiver = serializers.CharField(max_length=8)
    transfer_amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    commision = serializers.DecimalField(read_only=True, max_digits=11, decimal_places=2)
    status = serializers.ChoiceField(read_only=True, choices=Transactions.STATUS_TYPE)
    timestamp = serializers.DateTimeField(read_only=True, format="%Y.%m.%d %H:%M:%S")