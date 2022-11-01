

from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Currency(models.TextChoices):
    USD = 'USD'
    EUR = 'EUR'
    UAH = 'UAH'

class Wallet(models.Model):
    name = models.CharField(verbose_name='name', max_length=8)
    VISA = 'VISA'
    MASTER_CARD = 'MASTER_CARD'
    CARD_TYPE = [
        (VISA, 'visa card'),
        (MASTER_CARD, 'master card card'),
    ]
    type = models.CharField(verbose_name='type', max_length=11, choices=CARD_TYPE, default=VISA)
    currency = models.CharField(verbose_name='currency', max_length=3, choices=Currency.choices, default=Currency.USD)
    balance = models.DecimalField(verbose_name='balance', max_digits=11, decimal_places=2)
    user_id = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    created_on = models.DateTimeField(verbose_name='creating_time', auto_now_add=True)
    modefied_on = models.DateTimeField(verbose_name='modefied_time', auto_now=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    sender = models.ForeignKey('Wallet', verbose_name='sender', related_name='to_sender',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey('Wallet', verbose_name='receiver', related_name='from_receiver',
                                 on_delete=models.CASCADE)
    transfer_amount = models.DecimalField(verbose_name='transfer_amount', max_digits=11, decimal_places=2)
    commision = models.DecimalField(verbose_name='commision', max_digits=11, decimal_places=2)
    PAID = 'PAID'
    FAILED = 'FAILED'
    STATUS_TYPE = [
        (PAID, 'PAID'),
        (FAILED, 'FAILED'),
    ]
    status = models.CharField(verbose_name='status', max_length=6, choices=STATUS_TYPE)
    timestamp = models.DateTimeField(verbose_name='timestamp', auto_now_add=True)

    def __str__(self):
        return f'tr_{self.pk}, sender - {self.sender}, receiver - {self.receiver}'

