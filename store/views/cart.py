from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from store.models.customers import Customer
from store.models.product import Product
from store.views.home import order_essentials, encapsul


class Cart(View):

    def get(self, request):
        data = cart_display(request)
        return render(request, 'cart.html', data)

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
  

def cart_display(request):
    ids = list(request.session.get('cart').keys())
    vals = list(request.session.get('cart').values())
    products = Product.get_products_by_id(ids)
    sum = 0

    cartlength = len(products)

    for i in range(cartlength):
        sum += (products[i].price * vals[i])

    tmp_c = Customer.objects.filter(id = request.session['customer'])

    if tmp_c[0].deal:
        request.session['cart_price'] = sum*(0.8)
    else:
        request.session['cart_price'] = sum

    status_data = order_essentials(request)
    data={}
    data = encapsul(request)
    data.update({'products': products})

    #Product Recommendation.
    cat_list = []
    for p in products:
        if (p.category.id not in cat_list):
            cat_list.append(p.category.id)
    products = list(products)
    print('products', products)
    select_products = []
    for i in cat_list:
        select_products.append(Product.get_orderedlist_by_category(i))
    print('hey...',select_products)
    arr = []
    for k in range(len(select_products)):
        arr += list(select_products[k])
        print('arr is .. ', arr)
    select_products = arr
    print(len(select_products))
        #if len(select_products[p]) == 1:
            #arr.append(len(select_products[i]))
    #select_products = arr
    recom_prod = []
    products = list(products)
    for p in range(len(select_products)):
        if select_products[p] not in products:
            recom_prod.append(select_products[p])
            print(select_products[p], type(select_products[p]))
    
    data.update({'recommended': recom_prod})
    return data