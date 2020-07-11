from django.contrib import admin

# Register your models here.
from employee_register.models import Employee, Postion

admin.site.register(Postion)
admin.site.register(Employee)