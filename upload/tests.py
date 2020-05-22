from django.test import TestCase


# Create your tests here.

import datetime
from django.utils import timezone
from HomeworkPublish.models import Homework
from upload.models import userfile
from django.contrib.auth.models import User

class uploadModelTests(TestCase):

    def test_upload(self):
        #创建ddl为过去时间的作业模型
        newhomework = Homework(
            courseNum = 1,
            Homework_title='test',
            Homework_text='test',
            )
        newuserfile = userfile(
            username = "user",
            homework = newhomework,
        )

        self.assertIs(newuserfile.returnhomeworkcourseNum(), 1)
