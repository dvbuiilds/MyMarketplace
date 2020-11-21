from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.customers import Customer
from store.models.product import Product
from store.models.orders import Order, change_status
from store.views.home import encapsul, order_essentials


class Wallet(View):
    def get(self, request):
        cid = request.session.get('customer')
        temp_c = Customer.get_obj_by_id(cid)
        data = {'balance': temp_c.wallet_balance}
        #print('paisa=',temp_c)
        
        request.session['balance'] = temp_c.wallet_balance
        print(temp_c.wallet_balance)
        return redirect('cart')

    def post(self, request):
        add_money = request.POST['addmoney']
        cid = request.session.get('customer')
        temp_c = Customer.get_obj_by_id(cid)
        temp_c.wallet_balance = temp_c.wallet_balance + float(add_money)
        request.session['balance'] = temp_c.wallet_balance
        temp_c.save()
        print(request.session['balance'])
        return redirect('cart')

        

