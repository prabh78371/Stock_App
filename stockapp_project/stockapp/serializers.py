from dataclasses import field, fields
from pyexpat import model
from unicodedata import category
from .models import Product,Inventory,Category,Transaction
from rest_framework import serializers

       
class Categoryserilizer(serializers.ModelSerializer):
    # product = serializers.HiddenField(default = 1)
    class Meta:
        model = Category
        fields = ['product','product_code','packs_per_carton']
        depth = 1


class Productserilizer(serializers.ModelSerializer):
    barcode_number = serializers.HiddenField(default = 1)
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
        depth = 0
