from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Products/',views.products,name="productapi"),
    path('Products/<int:barcode_number>',views.products,name="productapi"),
    path('Category/',views.category,name="categoryapi"),
    path('Category/<int:pk>',views.category,name="categoryapi"),
    path('Inventory/',views.inventory,name="inventory"),
    path('Transaction/',views.transaction,name="transaction"),
 


]
