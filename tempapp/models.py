from django.db import models

class Employee(models.Model):
    emp_name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.emp_name

class Hours(models.Model):
    emp_name = models.ForeignKey(Employee, on_delete=models.PROTECT)
    days = models.DateTimeField('date')
    hours = models.IntegerField

    def __int__(self):
        return self.days

class Salary(models.Model):
    days = models.ForeignKey(Hours, on_delete=models.PROTECT)
    Credeted_salary = models.IntegerField()
    salary_date = models.DateField()
