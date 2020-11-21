from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customers import Customer
from .models.sellers import Seller
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display=['name', 'price', 'seller', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['fname', 'lname', 'phone', 'email', 'password']

class AdminSeller(admin.ModelAdmin):
    list_display=['firmname', 'fname', 'lname', 'phone', 'email', 'password']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)
admin.site.register(Seller, AdminSeller)