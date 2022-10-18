from rest_framework import serializers
from .models import Wallet

class WalletSerialazer(serializers.Serializer):
    name = serializers.CharField(max_length=8, read_only=True)
    type = serializers.CharField(max_length=11)
    currency = serializers.CharField(max_length=3)
    balance = serializers.DecimalField(max_digits=11, decimal_places=2, read_only=True)
    user_id = serializers.CharField(read_only=True)
    created_on = serializers.DateTimeField(read_only=True)
    modefied_on = serializers.DateTimeField(read_only=True)