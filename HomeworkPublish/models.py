from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

# 作业模型，包含各项内容如下
class Homework(models.Model):
    #subject = models.ForeignKey(user, on_delete=models.CASCADE)
    Homework_title =models.TextField()
    Homework_text =models.TextField()
    courseNum = models.IntegerField()
    Pub_time = models.DateTimeField(default=timezone.now)
    deadline_date = models.TextField()
    deadline_time = models.TextField(default='23:59')

    class Meta:
        ordering = ('-Pub_time',)
    
    def __str__(self):
        return self.Homework_title
    
    def was_created_recently(self):
        # 若评论是"最近"发表的，则返回 True
        diff = timezone.now() - self.Pub_time
        if diff.days <= 0 and diff.seconds < 60:
            return True
        else:
            return False