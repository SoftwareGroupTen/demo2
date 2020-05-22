from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class normaluserform(models.Model):
    USER = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True,max_length=50)
    Identity = models.CharField(max_length=2)
    
    class Meta:
        verbose_name_plural = "normaluserform"
    
class course(models.Model):
    teacherName = models.CharField(max_length=10)
    courseNum = models.CharField(max_length=10)
    courseName = models.CharField(max_length=10)
    def __str__(self):
        return self.courseName
    def returncourseNum(self):
        return self.courseNum
class stucourse(models.Model):
    studentName = models.CharField(max_length=10)
    thecourse = models.ForeignKey('course',on_delete=models.CASCADE)

class asscourse(models.Model):
    assistantName = models.CharField(max_length=10)
    thecourse = models.ForeignKey('course',on_delete=models.CASCADE)