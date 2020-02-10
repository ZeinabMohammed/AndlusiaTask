from django.contrib import admin

from .models import(Department,
					Manager,
					Employee,
					Profile)
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Profile)