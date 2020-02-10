from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from django.contrib.auth.models import User

from .models import(Department,
					Manager,
					Employee,
					Profile)

class EmployeeSerializer(ModelSerializer):
	profile = HyperlinkedIdentityField(view_name='department:emp-detail', source='Employee')
	class Meta:
		model = Employee
		fields= ['emp_name','profile']


class ManagerSerializer(ModelSerializer):
	profile = HyperlinkedIdentityField(view_name='department:manager-detail', source='Manager')
	employees = EmployeeSerializer(many=True, read_only=True)

	class Meta:
		model = Manager
		fields= ['manager_name','profile','employees']
		depth = 3

class DepartmentSerializer(ModelSerializer):
	manager = ManagerSerializer(many=False)


	class Meta:
		model  = Department
		fields = ['dept_name','manager']
		depth = 3

class EmployeeProfileSerializer(ModelSerializer):
	
	class Meta:
		model  = Employee
		fields = ['profile']

class ManagerProfileSerializer(ModelSerializer):

	class Meta:
		model = Manager
		fields= ['profile']


