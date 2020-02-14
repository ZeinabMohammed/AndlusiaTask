from django.db import models
from django.contrib.auth.models import User


#Department table
class Department(models.Model):
	dept_name = models.CharField(max_length=20,blank=False,null=False)

	def __str__(self):
		return self.dept_name
	# def get_absolute_url(self):

	# 	return reverse("department_v1:department-detail", kwargs={"pk":self.pk})

#manager table
class Manager(models.Model):
	manager_name = models.CharField(max_length=20,blank=False,null=False)
	department   = models.OneToOneField(Department,on_delete=models.CASCADE,related_name='manager')#each dept has one manager
	profile      = models.URLField(max_length=200, unique=True,null=True)

	def __str__(self):
		return self.manager_name

#Employees table
class Employee(models.Model):
	emp_name = models.CharField(max_length=20,blank=False,null=False)
	manager  = models.ForeignKey(Manager,on_delete=models.CASCADE,related_name='employees')#manager has many employees
	profile  = models.URLField(max_length=200, unique=True,null=True)

	def __str__(self):
		return self.emp_name


