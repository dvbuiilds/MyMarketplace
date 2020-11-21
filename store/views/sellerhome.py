from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.sellers import Seller
from django.views import View


class SIndex(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        
        

    def get(self, request):
        # cart = request.session.get('cart')
        # if not cart:
        #     request.session['cart'] = {}
        # pdts = Product.get_all_products()
        # ctgrs = Category.get_all_categories()
        # categoryID = request.GET.get('category')
        # #print(type(pdts))
        # if categoryID:
        #     pdts = Product.get_all_products_by_categoryid(categoryID)

        # else:
        #     pdts = Product.get_all_products() 
        
        
        #print('you are ', request.session.get('email'))
        
        sellid = request.session.get('seller')
        print(sellid, type(sellid))
        data = {}

        if sellid:
            pdtlst = Product.get_all_products_by_seller(sellid)
            print(pdtlst)
            data['productlist'] = pdtlst
        
        else:
            print('No....')
        
        
        
        #print('you are ', request.session.get('email'))
        return render(request, 'sellerindex.html', data)






# Create your views here.
