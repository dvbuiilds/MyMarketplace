from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from datetime import datetime


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1 
            else:
                cart[product] = 1
        
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        return HttpResponseRedirect(request.path_info)


    def get(self, request):
        cart = request.session.get('cart')
        #cart = {}
        if not cart:
            request.session['cart'] = {}
        
        data = encapsul(request)
        return render(request, 'index.html', data)


def order_essentials(request):
    c_orders = request.session.get('c_orders')
    c_date = request.session.get('date_time')

    #Date import........
    arr = []
    if c_date:
        for x in c_date:
            arr.append(datetime.fromisoformat(x))
        c_date = arr
    
    #Order import ,.......
    if c_orders:
        temp_orders = Product.get_products_for_status(c_orders)
        return zip(temp_orders, c_date)

    else:
        return None
# Create your views here.

def encapsul(request):
    pdts = Product.get_all_products()
    ctgrs = Category.get_all_categories()
    categoryID = request.GET.get('category')

    if categoryID:
        pdts = Product.get_all_products_by_categoryid(categoryID)

    else:
        pdts = Product.get_all_products() 
    
    status_data = order_essentials(request)
    
    data = {}
    data['products'] = pdts
    data['categories'] = ctgrs
    data['corders'] = status_data
    return data

def termsofuse(request):

    return render(request, 'termsofuse.html')