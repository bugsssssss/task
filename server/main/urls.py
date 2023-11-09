from django.urls import path, include
from .views import *

urlpatterns = [
    path('statistics/employee/<int:id>/',
         EmployeeStatisticsView.as_view(), name='employee-statistics'),
    path('employee/statistics/', AllEmployeesStatisticView.as_view(),
         name='all-employees-statistics'),
    path('statistics/client/<int:id>/', ClientStatisticsView.as_view(),
         name='client-statistics'),
]
