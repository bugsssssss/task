from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.site_header = "Test"
admin.site.unregister(Group)