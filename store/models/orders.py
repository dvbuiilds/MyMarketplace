from django.db import models
from .product import Product
from .customers import Customer
import datetime as dt


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length = 100, default='', blank=True)
    phone = models.CharField(max_length= 12, default='', blank=True)
    date = models.DateTimeField(default = dt.datetime.today)
    status = models.BooleanField(default=False)
    
    
    def placeOrder(self, request):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer = customer_id)\
            .order_by('date')
    
    @staticmethod
    def get_product_id_by_customer(customer_id):
        if customer_id:
            return Order\
            .objects\
            .filter(customer = customer_id)\
            .order_by('date')\
            .values('product')
        
        else:
            return None

    @staticmethod
    def get_time_by_customer(customer_id):
        if customer_id:
            return Order\
            .objects\
            .filter(customer = customer_id)\
            .values('date')
        
        else:
            return None

def change_status(request, ord_arr):

    tmpo = []
    tmpd = []
    for x in ord_arr:
        tmpo.append(x.product.id)
        tmpd.append(str(x.date))
    request.session['c_orders'] = tmpo
    request.session['date_time'] = tmpd