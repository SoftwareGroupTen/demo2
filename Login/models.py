from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class 普通会员表(models.Model):
    用户 = models.OneToOneField(User, on_delete=models.CASCADE)
    昵称 = models.CharField(blank=True,max_length=50)
    身份 = models.CharField(max_length=2)
    
    class Meta:
        verbose_name_plural = "普通会员表"
    
class course(models.Model):
    teacherName = models.CharField(max_length=10)
    courseNum = models.CharField(max_length=10)
    courseName = models.CharField(max_length=10)
class stucourse(models.Model):
    studentName = models.CharField(max_length=10)
    thecourse = models.ForeignKey('course',on_delete=models.CASCADE)

class asscourse(models.Model):
    assistantName = models.CharField(max_length=10)
    thecourse = models.ForeignKey('course',on_delete=models.CASCADE)