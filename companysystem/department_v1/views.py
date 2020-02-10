
from rest_framework.viewsets import ModelViewSet,generics
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse, Http404

from department.models import(Department,
					Manager,
					Employee,
					Profile)

from .serializers import(EmployeeSerializer,
						ManagerSerializer,
						DepartmentSerializer,
						EmployeeProfileSerializer,
						ManagerProfileSerializer)


class ManagersList(APIView):

	"""
	List all Managers.
	"""
	def get(self, request, *args, **kwargs):
		#print("version:", request.version)
		queryset = Manager.objects.all()
		resultSet = ManagerSerializer(queryset, many=True,context={'request': request})
		return Response(resultSet.data)

class ManagersDetails(APIView):

   """
   Retrieve a Manager instance.
   """
   lookup_field       = 'profile'
   def get_object(self, pk):
       try:
           return Manager.objects.get(pk=pk)
       except Manager.DoesNotExist:
           raise Http404

   def get(self, request, *args, **kwargs):
       #print("version:",kwargs['version'])

       pk = kwargs['pk']
       manager = self.get_object(pk)

       serializer = ManagerSerializer(manager,context={'request': request})

       return Response(serializer.data)


class DepartmentListAPI(APIView):
	"""list all Departments """
	def get(self, request, format=None):
		# permission_classes = [AllowAny,]
		departments = Department.objects.all()
		serializer 	= DepartmentSerializer(departments, many=True,context={'request': request})
		return Response(serializer.data)


class DepartmentDetailAPI(APIView):
	"""Retrieve department instance"""
	def get_object(self,pk):
		try:
			return Department.objects.get(pk=pk)
		except Department.DoesNotExist:
			raise Http404
	def get(self, request,pk, format=None):
		department = self.get_object(pk)
		serializer = DepartmentSerializer(department,context={'request': request})
		return Response(serializer.data)


class EmployeeProfileAPI(APIView):
	"""Retrieve employee profile instance"""
	lookup_field       = 'profile'
	def get_object(self,pk):
		try:
			return Employee.objects.get(pk=pk)
		except Employee.DoesNotExist:
			raise Http404
	def get(self, request,pk, format=None):
		employee_profile = self.get_object(pk)
		serializer = EmployeeProfileSerializer(employee_profile,context={'request': request})
		return Response(serializer.data)

class ManagerProfileAPI(APIView):
	"""Retrieve Manager profile instance"""
	lookup_field       = 'profile'
	def get_object(self,pk):
		try:
			return Manager.objects.get(pk=pk)
		except Manager.DoesNotExist:
			raise Http404
	def get(self, request,pk, format=None):
		manager_profile = self.get_object(pk)
		serializer = ManagerProfileSerializer(manager_profile,context={'request': request})
		return Response(serializer.data)