from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customers import Customer


class Accounts(View):
    temp = Customer()
    def get(self, request):
        return render(request, 'accounts.html')
    
    def post(self, request):
        tmp = self.temp
        postdt = request.POST
        tmp.fname= postdt['fname']
        tmp.lname= postdt['lname']
        tmp.phone= postdt['phone']
        tmp.email = postdt['email']
        tmp.password = postdt['password']
        error_message = None

        error_message = self.validateCustomer()

        #saving
        if not error_message:
            tmp.password = make_password(tmp.password)
            tmp_cust = Customer(fname = tmp.fname, lname = tmp.lname, phone = tmp.phone, email = tmp.email, password = tmp.password)

            tmp_cust.register()
            return redirect('login')

        else:
            values = {
                'fname' : tmp.fname,
                'lname' : tmp.lname,
                'phone': tmp.phone,
                'email' : tmp.email,

            }
            data = {
                'error' : error_message,
                'values' : values
            }
            return render(request, 'accounts.html', data)
    
    def validateCustomer(self):
        error_message = None
        tmp = self.temp

        #validation
        if (not tmp.fname):
            error_message = 'first name required! '
        elif len(tmp.fname)<3:
            error_message = 'first name should be of more than 2 chars'
    
        elif tmp.isExist():
            error_message = 'Email is already in use'
        return error_message


