from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.site_header = "Test"
admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'quantity',
        'price',
        'created'
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'id',
        'employee',
        'created'
    ]
