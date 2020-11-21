from django.db import models
from .category import Category
from .sellers import Seller

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default = 1)
    description = models.CharField(max_length=200, default='', null = True, blank=True)
    image = models.ImageField(upload_to='product_imgs/')
    ratings = models.FloatField(default = 1.0)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_products_for_status(ids):
        c = []
        for i in ids:
            c.append(str(i))
        return Product.objects.filter(id__in = c)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        
        else:
            return Product.get_all_products()
    
    @staticmethod
    def get_all_products_by_seller(seller_id):
        if seller_id:
            return Product.objects.filter(seller = seller_id)
        
        else:
            return Product.get_all_products()

    @staticmethod
    def get_orderedlist_by_category(category_id):
        return Product\
            .objects\
            .filter(category = category_id)\
            .order_by('ratings')