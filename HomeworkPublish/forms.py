from django import forms
from .models import Homework
class HomeworkFrom(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('Homework_text','deadline_date','deadline_time')