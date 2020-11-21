"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from store.views.home import Index, termsofuse
from store.views.accounts import Accounts
from store.views.selleraccounts import SellerAccounts
from store.views.sellerlogin import SellerLogin, slogout
from store.views.sellerhome import SIndex
from store.views.login import Login, logout
from store.views.cart import Cart
from .views.checkout import CheckOut
from .views.wallet import Wallet
from .views.deal import Deal
from .views.orders import OrderView
from store.middlewares.auth import authmiddleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('accounts', Accounts.as_view(), name = 'accounts'),
    path('login', Login.as_view(), name = 'login'),
    path('logout', logout, name = 'logout'),
    path('cart', authmiddleware(Cart.as_view()), name = 'cart'),
    path('check-out', authmiddleware(CheckOut.as_view()), name = 'checkout'),
    path('wallet', authmiddleware(Wallet.as_view()), name = 'wallet'),
    path('deal', authmiddleware(Deal.as_view()), name = 'deal'),
    path('orders', authmiddleware(OrderView.as_view()), name = 'orders'),
    path('sellerindex', SIndex.as_view(), name = 'sellerindex'),
    path('selleraccounts', SellerAccounts.as_view(), name = 'selleraccounts'),
    path('sellerlogin', SellerLogin.as_view(), name = 'sellerlogin'),
    path('sellerlogout', slogout, name = 'sellerlogout'),
    path('termsofuse', termsofuse, name = 'termsofuse'),
]
