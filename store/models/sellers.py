from django.db import models



class Seller(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 50)
    firmname = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length = 10)
    email = models.EmailField()
    password = models.CharField(max_length = 500)

    def __str__(self):
        return self.firmname
        
    def register_sel(self):
        self.save()
    
    @staticmethod
    def get_sel_by_email(em):
        try:
            return Seller.objects.get(email = em)
        
        except:
            return False


    def isSExist(self):
        if Seller.objects.filter(email = self.email):
            return True
        return False