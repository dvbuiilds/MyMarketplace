from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customers import Customer
from store.models.orders import Order
import pickle
import os.path
from os import path

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def post(self, request):
        remail = request.POST['email']
        rpassword = (request.POST['password'])
        
        if Customer.get_obj_by_email(remail):
            customer = Customer.get_obj_by_email(remail)

            query_orders = Order.get_product_id_by_customer(customer.id)
            query_time = Order.get_time_by_customer(customer.id)
            orders = []
            ord_time = []

            for t in query_time:
                ord_time.append(str(t['date']))
            for order in query_orders:
                orders.append(order['product'])

            if (check_password(rpassword, customer.password)):
                request.session['customer'] = customer.id
                request.session['fname'] = customer.fname
                request.session['c_orders'] = orders
                request.session['date_time'] = ord_time
                request.session['balance'] = customer.wallet_balance
                request.session['adv_pay'] = customer.deal
                
                name = 'cust_' + str(request.session['customer'])
                save_path = 'store/cart-session/'
                completeName = os.path.join(save_path, name + ".pickle")

                if path.exists(completeName):
                    with open(completeName, 'rb') as handle:
                        request.session['cart'] = pickle.load(handle)
                
                if Login.return_url:
                    
                    return redirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Invalid Email or Password!"
                return render(request, 'login.html', {'error': error_message})
        else:
            error_message = "Invalid Email or Password!"
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    a = request.session['cart']
    name = 'cust_' + str(request.session['customer'])
    save_path = 'store/cart-session/'
    completeName = os.path.join(save_path, name + ".pickle")

    if (request.session['cart']):
        with open(completeName, 'wb') as handle:
            pickle.dump(a, handle, protocol = pickle.HIGHEST_PROTOCOL)
    
    else:
        if path.exists(completeName):
            os.remove(completeName)

    request.session.clear()
    return redirect('login')


