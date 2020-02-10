from rest_framework import routers
from django.urls import path,include

from .views import (ManagersView,
					DepartmentsView,
					ManagerProfile,
					EmployeeProfile,
					)

app_name='department'

router = routers.DefaultRouter()
router.register('managers', ManagersView)
router.register('departments',DepartmentsView)




urlpatterns = [
	path('', include(router.urls)),
	path('emp/<pk>',EmployeeProfile.as_view(),name='emp-detail'),
	path('manager/<pk>',ManagerProfile.as_view(),name='manager-detail'),
	
	]