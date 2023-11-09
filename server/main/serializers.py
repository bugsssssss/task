from rest_framework import serializers
from .models import *
from clients.models import *


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'id',
            'full_name',
            'birthdate',
        ]
