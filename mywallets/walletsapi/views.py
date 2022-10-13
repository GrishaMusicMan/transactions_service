from rest_framework import generics
from django.shortcuts import render
from .Serialazers import WalletSerialazer
from .models import Walet

class WalletsAPIView(generics.ListAPIView):
    queryset = Walet.objects.all()
    serializer_class = WalletSerialazer
