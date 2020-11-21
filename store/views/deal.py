from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.customers import Customer
from store.models.product import Product
from store.models.orders import Order, change_status
from store.views.home import encapsul, order_essentials


class Deal(View):
    def get(self, request):
        cid = request.session.get('customer')
        temp_c = Customer.get_obj_by_id(cid)
        data = {'balance': temp_c.wallet_balance, 'adv_pay': temp_c.deal}
        
        request.session['balance'] = temp_c.wallet_balance
        return redirect('cart', data)

    def post(self, request):
        
        if (request.session['balance'] >= (request.session['cart_price'] * 0.2)):
            temp_money = request.POST['okdeal']
            t = ''
            for x in temp_money:
                if (x != '₹' and x != ' '):
                    t += x
            temp_money = t
            cid = request.session.get('customer')
            temp_c = Customer.get_obj_by_id(cid)
            temp_c.wallet_balance = temp_c.wallet_balance - float(temp_money)
            request.session['balance'] = temp_c.wallet_balance
            temp_c.deal = True
            temp_c.save()
            request.session['balance'] = temp_c.wallet_balance
            request.session['adv_pay'] = temp_c.deal
            
            return redirect( 'cart' )

        else:
            
            return redirect('cart')

