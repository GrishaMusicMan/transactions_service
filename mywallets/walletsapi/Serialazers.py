from rest_framework import serializers
from .models import Walet

class WalletSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Walet
        fields = '__all__'