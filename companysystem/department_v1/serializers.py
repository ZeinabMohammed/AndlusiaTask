from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SlugRelatedField
from django.contrib.auth.models import User

from department.models import(Department,
								Manager,
								Employee,
								Profile)

class EmployeeSerializer(ModelSerializer):
	profile = HyperlinkedIdentityField(view_name='department_v1:employee-profile', source='Employee')
	class Meta:
		model = Employee
		fields= ['emp_name','profile']


class ManagerSerializer(ModelSerializer):
	url 	= HyperlinkedIdentityField(view_name='department_v1:manager-detail', source='Manager')
	profile = HyperlinkedIdentityField(view_name='department_v1:manager-profile', source='Manager')
	employees = EmployeeSerializer(many=True, read_only=True)
	class Meta:
		model = Manager
		fields= ['manager_name','url','profile','employees']
		depth = 3

class DepartmentSerializer(ModelSerializer):
	manager = ManagerSerializer(many=False)
	details = HyperlinkedIdentityField(view_name='department_v1:department-detail', source='Department')
	class Meta:
		model  = Department
		fields = ['dept_name','details','manager']
		depth = 3

class EmployeeProfileSerializer(ModelSerializer):
	
	class Meta:
		model  = Employee
		fields = ['profile']

class ManagerProfileSerializer(ModelSerializer):
	class Meta:
		model = Manager
		fields= ['profile']


