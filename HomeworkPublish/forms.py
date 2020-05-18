from django import forms
from .models import Homework

#作业发布的提交表单
class HomeworkFrom(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('Homework_text','deadline_date','deadline_time')