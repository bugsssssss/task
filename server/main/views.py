from django.shortcuts import render
from rest_framework import generics, views, status
from rest_framework.response import Response
from clients.models import *
from .models import *
from django.db.models import Q, Prefetch, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404

# Можно вынести как отдельную функцию и передавать объект


def get_employee_data(employee, month, year):
    if month and year:
        try:
            related_orders = Order.objects.filter(
                employee=employee,
                created__year=year,
                created__month=month
            ).select_related('employee', 'client')
        except ValueError:
            related_orders = Order.objects.filter(
                employee=employee).select_related('employee', 'client')
    else:
        related_orders = Order.objects.filter(
            employee=employee).select_related('employee', 'client')

    # Для уникальных клиентов связанных с работником
    employee_clients = related_orders.values('client').distinct()

    # Для всех заказов связянных с работником
    employee_orders = related_orders.all()

    # Общая сумма
    total_price = related_orders.aggregate(
        total_price=Sum('products__price')
    )['total_price'] or 0

    data = {
        'id': employee.id,
        'full_name': employee.full_name,
        'clients_count': len(employee_clients),
        'orders_count': len(employee_orders),
        'total_price': total_price,
    }

    return data


class EmployeeStatisticsView(views.APIView):
    def get(self, request, id, *args, **kwargs):
        month = request.GET.get('month') or ''
        year = request.GET.get('year') or ''

        # Можно также использовать try, catch
        employee_instance = get_object_or_404(Employee, id=id)

        data = get_employee_data(employee_instance, month, year)

        return Response(
            data,
            status=status.HTTP_200_OK
        )


class AllEmployeesStatisticView(views.APIView):
    def get(self, request, *args, **kwargs):
        month = request.GET.get('month') or ''
        year = request.GET.get('year') or ''

        employee_instances = Employee.objects.all()
        all_data = [get_employee_data(x, month, year)
                    for x in employee_instances]

        return Response(all_data, status=status.HTTP_200_OK)


class ClientStatisticsView(views.APIView):
    def get(self, request, id, *args, **kwargs):
        month = request.GET.get('month') or ''
        year = request.GET.get('year') or ''

        # Можно также использовать try, catch
        client_instance = get_object_or_404(Client, id=id)

        # Тут также можно отдельно вынести как функцию, если к примеру нужно будет для всех клиентов выводить
        if month and year:
            try:
                related_orders = Order.objects.filter(
                    client=client_instance,
                    created__year=year,
                    created__month=month
                ).select_related('client', 'employee')
            except ValueError:
                related_orders = Order.objects.filter(
                    client=client_instance).select_related('client', 'employee')
        else:
            related_orders = Order.objects.filter(
                client=client_instance).select_related('client', 'employee')

        total_price = related_orders.aggregate(
            total_price=Sum('products__price')
        )['total_price'] or 0

        data = {
            'id': client_instance.id,
            'full_name': client_instance.full_name,
            'orders_count': len(related_orders),
            'total_price': total_price
        }

        return Response(
            data,
            status=status.HTTP_200_OK
        )
