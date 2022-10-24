"""mywallets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from walletsapi.views import (
    WalletsAPIView,
    WalletsByName,
    TransactionsByID,
    TransactionsByWalletsName,
    CreateTransaction
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf-auth/', include('rest_framework.urls')),
    path('wallets/', WalletsAPIView.as_view()),
    path('wallets/transactions/', CreateTransaction.as_view()),
    path('wallets/<str:namewalleturl>/', WalletsByName.as_view()),
    path('wallets/transactions/<int:tran_id>/', TransactionsByID.as_view()),
    path('wallets/transactions/<str:wallet_name>/', TransactionsByWalletsName.as_view())

]
