from django.db import models
from ac_login.models import LoginUser


class Department(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    def __str__(self):
        return self.name


class Officer(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='officer/')
    contact = models.IntegerField()
    username = models.ForeignKey(LoginUser,on_delete=models.CASCADE)