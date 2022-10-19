from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from random import choice
from .serialazers import WalletSerialazer
from .models import Wallet
from .models import User
from string import ascii_uppercase, digits


class WalletsAPIView(APIView):

    def get(self, request):
        lst = Wallet.objects.all()
        return Response(WalletSerialazer(lst, many=True).data)

    def post(self, request):
        serializer = WalletSerialazer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Wallet.objects.create(
            name=self.create_wallet_name(),
            type=request.data['type'],
            currency=request.data['currency'],
            balance=self.start_sum(request),
            user_id=User(1)
        )
        return Response(WalletSerialazer(post_new).data)

    def create_wallet_name(self):
        return ''.join([choice(ascii_uppercase + digits) for _ in range(8)])

    def start_sum(self, request):
        if request.data['currency'] == "USD" or request.data['currency'] == "EUR":
            return 3
        else:
            return 100


class WalletsAPIName(APIView):

    def get(self, request, namewalleturl):
        lst = Wallet.objects.get(name=namewalleturl)
        return Response(WalletSerialazer(lst).data)

    def delete(self, request, namewalleturl):
        wlt = Wallet.objects.get(name=namewalleturl)
        wlt.delete()
        return Response({"delete": "success"})

# class WalletsAPIView(generics.ListAPIView):
#
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerialazer
