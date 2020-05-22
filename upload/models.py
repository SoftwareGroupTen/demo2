from django.db import models
from HomeworkPublish.models import Homework
# Create your models here.

# Create your models here.
class userfile(models.Model):
    username = models.CharField(max_length = 30)
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
    )
    headImg = models.FileField(upload_to= './files/')
    #所以是用upload_to来指定文件存放的前缀路径
    def __str__(self):
        return self.homework.Homework_Text
    
    def returnhomeworkcourseNum(self):
        return self.homework.courseNum
