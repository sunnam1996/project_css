from django.db import models
from ac_login.models import LoginUser
from ac_admin.models import Department


class CitizenRegister(models.Model):
    ct_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='citizen/')
    username = models.ForeignKey(LoginUser,on_delete=models.CASCADE)
    otp = models.CharField(max_length=30)
    status = models.CharField(max_length=50)


class Complaints(models.Model):
    cid = models.IntegerField(primary_key=True)
    ct_id = models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='complaints/')
    register_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)
    close_date = models.DateField(null=True)


class Feedback(models.Model):
    fid = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Complaints,on_delete=models.CASCADE)
    ct_id = models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='feedback/')


class Reply_feedback(models.Model):
    re_no = models.AutoField(primary_key=True)
    fid = models.ForeignKey(Feedback,on_delete=models.CASCADE)
    cid = models.ForeignKey(Complaints,on_delete=models.CASCADE)
    ct_id = models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    message = models.TextField()