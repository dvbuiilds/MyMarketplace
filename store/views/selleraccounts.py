from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.sellers import Seller


class SellerAccounts(View):
    temp = Seller()
    def get(self, request):
        return render(request, 'selleraccounts.html')
    
    def post(self, request):
        tmp = self.temp
        postdt = request.POST
        tmp.firmname= postdt['firmname']
        tmp.fname= postdt['fname']
        tmp.lname= postdt['lname']
        tmp.phone= postdt['phone']
        tmp.email = postdt['email']
        tmp.password = postdt['password']
        error_message = None

        error_message = self.validateSeller()

        #saving
        if not error_message:
            tmp.password = make_password(tmp.password)
            tmp_sel = Seller(firmname = tmp.firmname, fname = tmp.fname, lname = tmp.lname, phone = tmp.phone, email = tmp.email, password = tmp.password)

            tmp_sel.register_sel()
            return redirect('sellerindex')

        else:
            svalues = {
                'firmname' : tmp.firmname,
                'fname' : tmp.fname,
                'lname' : tmp.lname,
                'phone': tmp.phone,
                'email' : tmp.email,

            }
            data = {
                'error' : error_message,
                'values' : svalues
            }
            return render(request, 'selleraccounts.html', data)
    
    def validateSeller(self):
        error_message = None
        tmp = self.temp

        #validation
        if (not tmp.firmname):
            error_message = 'first name required! '
        elif len(tmp.firmname)<3:
            error_message = 'first name should be of more than 2 chars'
    
        elif tmp.isSExist():
            error_message = 'Email is already in use'
        return error_message


