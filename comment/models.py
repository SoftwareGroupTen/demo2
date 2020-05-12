from django.db import models
from django.contrib.auth.models import User
from upload.models import userfile

class Comment(models.Model):
    userfile = models.ForeignKey(
        userfile,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    point = models.FloatField(null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]