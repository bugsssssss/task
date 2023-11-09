from django.contrib import admin
from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'id',
        'birthdate',
        'created',
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'id',
        'birthdate',
        'created',
    ]
