from django.contrib import admin

# Register your models here.
from employee.models import Employee

class EmployeeDesc(admin.ModelAdmin):
    list_display = ('eid', 'ename', 'eemail', 'econtact')

admin.site.register(Employee, EmployeeDesc)