import decimal
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from random import choice
from .serialazers import WalletSerialazer, TransactionSerialazer
from .models import Wallet, Transactions
from .models import User
from string import ascii_uppercase, digits


class WalletsAPIView(APIView):

    def get(self, request):
        lst = Wallet.objects.filter(user_id=self.request.user.id)
        return Response(WalletSerialazer(lst, many=True).data)

    def post(self, request):
        serializer = WalletSerialazer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not len(Wallet.objects.filter(user_id=request.user)) > 4:
            post_new = Wallet.objects.create(
                name=self.create_wallet_name(),
                type=request.data['type'].upper(),
                currency=request.data['currency'],
                balance=self.start_sum(request),
                user_id=User(self.request.user.id)
            )
            return Response(WalletSerialazer(post_new).data)
        else:
            return Response({"detail": "you can't have more than 5 wallets"})

    def create_wallet_name(self):
        return ''.join([choice(ascii_uppercase + digits) for _ in range(8)])

    def start_sum(self, request):
        if request.data['currency'] == "USD" or request.data['currency'] == "EUR":
            return 3
        else:
            return 100


class WalletsByName(APIView):

    def get(self, request, namewalleturl):
        lst = Wallet.objects.filter(user_id=self.request.user.id)
        wlt = Wallet.objects.get(name=namewalleturl)
        if wlt in lst:
            return Response(WalletSerialazer(wlt).data)
        else:
            return Response({"error": "You don't have access"})

    def delete(self, request, namewalleturl):
        lst = Wallet.objects.filter(user_id=self.request.user.id)
        wlt = Wallet.objects.get(name=namewalleturl)
        if wlt in lst:
            wlt.delete()
            return Response({"delete": "success"})
        else:
            return Response({"error": "You don't have access"})


class CreateTransaction(APIView):

    def get(self, request):
        user_wallets = Wallet.objects.filter(user_id=self.request.user.id)
        lst = Transactions.objects.filter(
            Q(sender__in=user_wallets) | Q(receiver__in=user_wallets)
        )

        return Response(TransactionSerialazer(lst, many=True).data)

    def post(self, request):
        serializer = TransactionSerialazer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if self.check_current(request):
            if self.check_balance(request):

                tran_new = Transactions.objects.create(
                    sender=Wallet.objects.get(name=request.data['sender']),
                    receiver=Wallet.objects.get(name=request.data['receiver']),
                    transfer_amount=request.data['transfer_amount'],
                    commision=self.get_commission(request),
                    status='PAID'
                )

                sender = Wallet.objects.get(name=request.data['sender'])
                receiver = Wallet.objects.get(name=request.data['receiver'])
                sender.balance -= decimal.Decimal(request.data['transfer_amount']) + self.get_commission(request)
                sender.save()
                receiver.balance += decimal.Decimal(request.data['transfer_amount'])
                receiver.save()

                return Response(TransactionSerialazer(tran_new).data)
            else:
                return Response({"detail": "not enough money"})
        else:
            return Response({"detail": "transactions are available only for wallets with the same currency"})

    def check_current(self, request):
        sender = Wallet.objects.get(name=request.data['sender'])
        receiver = Wallet.objects.get(name=request.data['receiver'])
        return sender.currency == receiver.currency

    def check_balance(self, request):
        sender = Wallet.objects.get(name=request.data['sender'])
        transfer_amount = request.data['transfer_amount']
        return sender.balance - decimal.Decimal(transfer_amount) >= 0

    def get_commission(self, request):
        sender = Wallet.objects.get(name=request.data['sender'])
        receiver = Wallet.objects.get(name=request.data['receiver'])
        transfer_amount = request.data['transfer_amount']

        if sender.user_id == receiver.user_id:
            return 0
        else:
            return decimal.Decimal(transfer_amount) * decimal.Decimal(0.1)


class TransactionsByID(APIView):

    def get(self, request, tran_id):
        lst = Transactions.objects.get(pk=tran_id)
        return Response(TransactionSerialazer(lst).data)


class TransactionsByWalletsName(APIView):

    def get(self, request, wallet_name):
        wallet = Wallet.objects.get(name=wallet_name)
        queryset = Transactions.objects.filter(
            Q(sender=wallet.id) | Q(receiver=wallet.id)
        )
        return Response(TransactionSerialazer(queryset, many=True).data)
