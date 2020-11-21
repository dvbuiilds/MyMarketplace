from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.sellers import Seller 


class SellerLogin(View):
    return_url = None

    def get(self, request):
        self.return_url = request.GET.get('return_url')
        print(self.return_url)
        return render(request, 'sellerlogin.html')
    
    def post(self, request):
        error_message = None
        remail = request.POST['email']
        rpassword = (request.POST['password'])
        
        seller = Seller.get_sel_by_email(remail)
        print((seller.id))
        if seller:
            if (check_password(rpassword, seller.password)):
                request.session['seller'] = seller.id
                if self.return_url:
                    
                    return redirect(self.return_url)
                else:
                    #print(self.return_url)
                    self.return_url = None
                    return redirect('sellerindex')

        else:
            error_message = "Invalid Email or Password!"
        return render(request, 'sellerindex.html', {'error': error_message})

def slogout(request):
    request.session.clear()
    return redirect('sellerindex')


