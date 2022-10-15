from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
import random
from .Serialazers import WalletSerialazer
from .models import Walet
from .models import User

class WalletsAPIView(APIView):

    def get(self, request):
        lst = Walet.objects.all().values()
        return Response(list(lst))

    def post(self, request):
        post_new = Walet.objects.create(
            name=self.create_wallet_name(),
            type=request.data['type'],
            currency=request.data['currency'],
            balance=3,
            user_id=User(1)
        )
        return Response({'post': model_to_dict(post_new)})

    def create_wallet_name(self):
        simbols = 'QWERTYUIOPLKJHGFDSAZXCVBNM0123456789'
        new_name = []
        while len(new_name) < 8:
            new_name.append(simbols[random.randint(0, len(simbols) - 1)])
        return ''.join(new_name)






# class WalletsAPIView(generics.ListAPIView):
#
#     queryset = Walet.objects.all()
#     serializer_class = WalletSerialazer
