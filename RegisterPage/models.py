from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=15)
    empsalary=models.IntegerField()
    empphno=models.IntegerField()
    empaddress=models.CharField(max_length=100)

    def __str__(self):
        return self.empname
