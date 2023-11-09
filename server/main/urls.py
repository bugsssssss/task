from django.urls import path, include
from .views import *

urlpatterns = [
    path('statistics/employee/<int:id>/',
         EmployeeStatisticsView.as_view(), name='employee-statistics')
]
