from django.db import models

class LoginUser(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    type_user = models.CharField(max_length=50)