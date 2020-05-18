from django.db import models
from Login.models import normaluserform
from upload.models import userfile

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

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]