from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.customers import Customer
from store.models.sellers import Seller
from store.models.product import Product
from store.models.orders import Order



class Addproduct(View):
    
    def post(self, request):
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        quantity = request.POST['quantity']
        seller = request.session.get('seller')
        prodlist = request.session.get('prodlist')
        products = Product.get_all_products_by_seller(list(prodlist.keys()))

        for product in products:
            order = Order(seller = Seller(id = seller), product = product, price = product.price, quantity = prodlist.get(str(product.id)), )
            order.placeOrder()

        request.session['cart'] = {}
        #print(address, phone, customer, cart, products)
        return redirect('cart')


