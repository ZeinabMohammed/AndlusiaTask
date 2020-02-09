from django.db import models
from django.contrib.auth.models import User


#Department table
class Department(models.Model):
	name = models.CharField(max_length=20,blank=False,null=False)
	# employee= models.CharField(max_length=20,blank=False,null=False)

	def __str__(self):
		return self.name


class Manager(models.Model):
	name       = models.CharField(max_length=20,blank=False,null=False)
	department = models.OneToOneField(Department,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Employee(models.Model):
	name       = models.CharField(max_length=20,blank=False,null=False)
	manager    = models.ForeignKey(Manager,on_delete=models.CASCADE)
	# department = models.ForeignKey(Department,on_delete=models.CASCADE)
	

	def __str__(self):
		return self.name

#Profile Table
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	def __str__(self):
		return self.user