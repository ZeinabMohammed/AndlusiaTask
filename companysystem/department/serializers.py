from rest_framework.serializers import ModelSerializer
from .models import(Department,
					Manager,
					Employee,
					Profile)

class EmployeeSerializer(ModelSerializer):
	
	class Meta:
		model = Employee
		fields= ['name']


class ManagerSerializer(ModelSerializer):
	name      = serializers.CharField()
	employees = EmployeeSerializer(many=True)

	class Meta:
		model = Manager
		fields= ['name','employees']


class DepartmentSerializer(ModelSerializer):
	manager   = ManagerSerializer(many=False)
	# employees = EmployeeSerializer(many=True, read_only=True)

	class Meta:
		model  = Department
		fields = ['name','manager']