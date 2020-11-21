from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.sellers import Seller
from store.models.product import Product
from store.models.listofproducts import LIST



class ProductListView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders.reverse()})

