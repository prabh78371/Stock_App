from dataclasses import field, fields
from pyexpat import model
from unicodedata import category
from .models import Product,Inventory,Category,Transaction
from rest_framework import serializers

       
class Categoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['product_code','packs_per_carton']
        depth = 1


class Productserilizer(serializers.ModelSerializer):
    category_set = Categoryserilizer(many=True,read_only= True)
    class Meta:
        model = Product
        fields = ['name','category_set']
        

class Inventoryserilizer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['product','quantity']
        depth = 2

class Transactionserilizer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 3
