from django.db import models


class Customer(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    email = models.EmailField()
    password = models.CharField(max_length = 500)
    wallet_balance = models.FloatField(default=0)
    deal = models.BooleanField(default=False)
    
    def register(self):
        self.save()
    
    @staticmethod
    def get_obj_by_email(em):
        try:
            return Customer.objects.get(email = em)
        
        except:
            return False

    @staticmethod
    def get_obj_by_id(i):
        try:
            return Customer.objects.get(id = i)
        
        except:
            return False

    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    
def change_wallet(cid, amt, request):
    customer = Customer.objects.get(id = cid)
    customer.wallet_balance -= amt
    customer.save()
    request.session['balance'] = customer.wallet_balance