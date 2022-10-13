from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Walet(models.Model):
    name = models.CharField(verbose_name='name', max_length=8)
    VISA = 'VISA'
    MASTER_CARD = 'MASTER_CARD'
    CARD_TYPE = [
        (VISA, 'visa card'),
        (MASTER_CARD, 'master card card'),
    ]
    type = models.CharField(verbose_name='type', max_length=11, choices=CARD_TYPE, default=VISA)
    USD = 'USD'
    EUR = 'EUR'
    UAH = 'UAH'
    CURRENCY_TYPE = [
        (USD, 'Dollars'),
        (EUR, 'Euro'),
        (UAH, 'Hryvnia'),
    ]
    currency = models.CharField(verbose_name='currency', max_length=3, choices=CURRENCY_TYPE, default=USD)
    balance = models.DecimalField(verbose_name='balance', max_digits=11, decimal_places=2)
    user_id = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    created_on = models.DateTimeField(verbose_name='creating_time', auto_now_add=True)
    modefied_on = models.DateTimeField(verbose_name='modefied_time', auto_now=True)

# class Transactions(models.Model):
#     sender = models.CharField(verbose_name='sender', max_length=8)
#     receiver = models.CharField(verbose_name='receiver', max_length=8)
#     transer_amount = models.DecimalField(verbose_name='transer_amount', decimal_places=2)
#     commision = models.DecimalField(verbose_name='commision', decimal_places=2)
#     STATUS_TYPE = (
#         ('PAID ', 'PAID '),
#         ('FAILED', 'FAILED'),
#     )
#     status = models.CharField(verbose_name='status', choices=STATUS_TYPE)
#     timestamp = models.DateTimeField(verbose_name='timestamp', auto_now_add=True)
