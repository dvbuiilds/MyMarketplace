from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.orders import Order
from store.views.home import order_essentials, encapsul
#from store.middlewares.auth import authmiddleware
#from django.utils.decorators import method_decorator


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer) 
        data = encapsul(request)
        data.update({'orders': orders.reverse()})
        return render(request, 'orders.html', data)

