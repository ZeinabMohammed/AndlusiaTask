
from rest_framework.viewsets import ModelViewSet,generics
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse, Http404

from .models import(Department,
					Manager,
					Employee,
					Profile)

from .serializers import(EmployeeSerializer,
						ManagerSerializer,
						DepartmentSerializer,
						EmployeeProfileSerializer,
						ManagerProfileSerializer)


class ManagersView(ModelViewSet):
	"""List All Managers"""
	queryset = Manager.objects.all()
	serializer_class = ManagerSerializer

class DepartmentsView(ModelViewSet):
	"""List All Departments """
	queryset 		 = Department.objects.all()
	serializer_class = DepartmentSerializer

class EmployeeProfile(generics.RetrieveAPIView):
	"""Retrieve  employee profile instance"""
	permission_classes = (IsAuthenticated,)
	queryset 		   = Employee.objects.all()
	serializer_class   = EmployeeSerializer
	lookup_field       = 'profile'

class ManagerProfile(generics.RetrieveAPIView):
	"""retrieve Manager ProFilesinstance"""
	permission_classes = (IsAuthenticated,)
	queryset 		   = Manager.objects.all()
	serializer_class   = ManagerSerializer
	lookup_field       = 'profile'

