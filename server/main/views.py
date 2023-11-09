from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.response import Response
from clients.models import *
from .models import *
from django.db.models import Q, Prefetch, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count


class EmployeeStatisticsView(views.APIView):
    def get(self, request, id, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')
        try:
            employee_instance = Employee.objects.get(Q(id=id))
        except ObjectDoesNotExist:
            return Response({'error': 'Нет работника с таким айди'}, status=status.HTTP_404_NOT_FOUND)

        employee_clients = Order.objects.filter(
            employee=employee_instance).select_related('employee', 'client').values('client').distinct()

        employee_orders = Order.objects.filter(
            employee=employee_instance).select_related('employee', 'client').all()

        total_price = Order.objects.filter(employee=employee_instance).aggregate(
            total_price=Sum('products__price')
        )['total_price'] or 0

        return Response(
            {
                'full_name': employee_instance.full_name,
                'clients_count': len(employee_clients),
                'orders_count': len(employee_orders),
                'total_price': total_price
            },
            status=status.HTTP_200_OK
        )


class AllEmployeesStatisticView(views.APIView):
    def get(self, request, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')
        # 
        #
        #
        return Response({'test': 'test'})
