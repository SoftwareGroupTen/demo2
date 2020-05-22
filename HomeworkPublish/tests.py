from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from HomeworkPublish.models import Homework
from django.contrib.auth.models import User

class HomeworkModelTests(TestCase):

    def test_was_created_recently_with_future(self):
        #创建ddl为过去时间的作业模型
        newhomework = Homework(
            courseNum = 1,
            Homework_title='test',
            Homework_text='test',
            )

        self.assertIs(newhomework.was_created_recently(), True)
