from django.contrib import admin
from .models import Product

# Register your models here.

class productAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, productAdmin)

