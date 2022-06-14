from django.contrib import admin
from .models import Category, Product,Transaction,Inventory,Customuser

# Register your models here.
admin.site.register(Customuser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Inventory)