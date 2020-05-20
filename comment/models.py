from django.db import models
from Login.models import normaluserform
from upload.models import userfile
from django.utils import timezone

#评论的模型
class Comment(models.Model):
    userfile = models.ForeignKey(
        userfile,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    commentator = models.CharField(max_length=10)
    point = models.FloatField(null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def was_created_recently(self):
        # 若评论是"最近"发表的，则返回 True
        diff = timezone.now() - self.created
        if diff.days <= 0 and diff.seconds < 60:
            return True
        else:
            return False

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]