from django.contrib import admin
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'type', 'brand', 'price', 'available', 'description')  
    search_fields = ('name', 'type', 'brand')  

admin.site.register(Products,ProductAdmin)
