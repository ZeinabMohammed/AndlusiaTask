from rest_framework import routers
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

from .views import (ManagersList,
					ManagersDetails,
					DepartmentListAPI,
					DepartmentDetailAPI,
					EmployeeProfileAPI,
					ManagerProfileAPI,
					)

app_name='department_v1'

urlpatterns = [
	path('managers',ManagersList.as_view(),name='managers-list'),
	path('manager/<pk>',ManagersDetails.as_view(),name='manager-detail'),
	path('',DepartmentListAPI.as_view(),name='departments-list'),
	path('department/<pk>',DepartmentDetailAPI.as_view(),name='department-detail'),
	path('emp-profile/<pk>',EmployeeProfileAPI.as_view(),name='employee-profile'),
	path('manager-profile/<pk>',ManagerProfileAPI.as_view(),name='manager-profile'),
	
	]