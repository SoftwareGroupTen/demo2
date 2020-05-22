from django.test import TestCase

# Create your tests here.

import datetime
from .models import Comment
from upload.models import userfile
from HomeworkPublish.models import Homework
from django.utils import timezone

class CommmentModelTests(TestCase):

    def test_was_created_recently_with_future(self):
        #创建ddl为过去时间的作业模型
        homework1 = Homework(Homework_title="test1")
        comment = Comment(
            userfile = userfile(username="user",homework=homework1),
            commentator = 'assistant1',
            point = 100,
            body = 'test',
            created=timezone.now()+datetime.timedelta(days=30),
            )
        self.assertIs(comment.was_created_recently(), True)
