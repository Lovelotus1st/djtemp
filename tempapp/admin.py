from django.contrib import admin
from tempapp.models import Employee,Hours,Salary
# Register your models here.
admin.site.register(Employee)
admin.site.register(Hours)
admin.site.register(Salary)