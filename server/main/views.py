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


class EmployeeStatisticsView(views.APIView):
    def get(self, request, id, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')

        if month and year:
            try:
                employee_data = Employee.objects.filter(
                    id=id,
                    order__created__month=month,
                    order__created__year=year
                ).annotate(
                    clients_count=Count('order__client', distinct=True),
                    orders_count=Count('order', distinct=True),
                    total_price=Sum('order__products__price')
                ).values('full_name', 'clients_count', 'orders_count', 'total_price').first()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            employee_data = Employee.objects.filter(id=id).annotate(
                clients_count=Count('order__client', distinct=True),
                orders_count=Count('order', distinct=True),
                total_price=Sum('order__products__price')
            ).values('full_name', 'clients_count', 'orders_count', 'total_price').first()

        return Response(employee_data, status=status.HTTP_200_OK)


class AllEmployeesStatisticView(views.APIView):
    def get(self, request, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')

        if month and year:
            try:
                employee_data = Employee.objects.filter(
                    order__created__month=month, order__created__year=year
                ).annotate(
                    clients_count=Count('order__client', distinct=True),
                    orders_count=Count('order', distinct=True),
                    total_price=Sum('order__products__price')
                ).values('id', 'full_name', 'clients_count', 'orders_count', 'total_price')
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

        else:
            employee_data = Employee.objects.all().annotate(
                clients_count=Count('order__client', distinct=True),
                orders_count=Count('order', distinct=True),
                total_price=Sum('order__products__price')
            ).values('id', 'full_name', 'clients_count', 'orders_count', 'total_price')

        employee_data_list = list(employee_data)
        return Response(employee_data_list, status=status.HTTP_200_OK)


class ClientStatisticsView(views.APIView):
    def get(self, request, id, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')

        if month and year:
            try:
                client_instance = Client.objects.filter(
                    id=id,
                    order__created__month=month,
                    order__created__year=year
                ).annotate(
                    orders_count=Count('order', distinct=True),
                    total_price=Sum('order__products__price')
                ).values('full_name', 'orders_count', 'total_price').first()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

        else:
            client_instance = Client.objects.filter(
                id=id,
            ).annotate(
                orders_count=Count('order', distinct=True),
                total_price=Sum('order__products__price')
            ).values('full_name', 'orders_count', 'total_price').first()

        return Response(
            client_instance,
            status=status.HTTP_200_OK
        )
