from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.customers import Customer, change_wallet
from store.models.product import Product
from store.models.orders import Order, change_status
from store.views.home import encapsul, order_essentials
from store.views.cart import cart_display


class CheckOut(View):
    
    def post(self, request):
        address = request.POST['address']
        phone = request.POST['phone']
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        vals = list(request.session.get('cart').values())

        products = Product.get_products_by_id(list(cart.keys()))
        cartlength = len(products)
        
        sum = request.session['cart_price']
        amt = request.session.get('balance')
        
        
        error_message = None
        if ( amt >= sum):
            for product in products:
                order = Order(customer = Customer(id = customer), product = product, price = product.price, quantity = cart.get(str(product.id)), phone = phone, address = address)
                order.placeOrder(request)
            

            ord_arr = []
            for product in products:
                ord_arr.append(Order(customer = Customer(id = customer), product = product, price = product.price, quantity = cart.get(str(product.id)), phone = phone, address = address))
            
            change_status(request, ord_arr)
            tempc = Customer.get_obj_by_id(customer)
            if tempc.deal:
                tempc.deal = False
                request.session['adv_pay'] = False
                tempc.save()
            change_wallet(request.session['customer'], sum, request)
            request.session['cart'] = {}
            request.session['cart_price'] = 0
            
            return redirect('cart')
        
        else:
            data = cart_display(request)
            error_message = "You have Insufficient balance! Add more money to shop."
            data.update({'error': error_message})
            return render(request, 'cart.html', data)


