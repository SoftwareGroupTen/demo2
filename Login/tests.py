from django.test import TestCase

# Create your tests here.

from Login.models import course


class courseModelTests(TestCase):

    def test_coursemodel(self):
        
       
        newcourse = course(
            courseNum = 1,
            courseName = 'test'
            )

        self.assertIs(newcourse.returncourseNum(), 1)