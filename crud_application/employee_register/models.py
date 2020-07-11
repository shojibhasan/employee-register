from django.db import models

# Create your models here.

class Postion(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    position = models.ForeignKey(Postion,on_delete=models.CASCADE)