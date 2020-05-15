from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

class customizedloginForm(AuthenticationForm):
    VerificationCode = CaptchaField()

class customizededitForm(UserChangeForm):
    nickname = forms.CharField(required=False,max_length=50)
    Identity = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','password','email','nickname','Identity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique':'该用户名已存在！' , 'invalid':'该用户名格式不符合要求！'}


class customizedregisterForm(UserCreationForm):
    nickname = forms.CharField(required=False,max_length=50)
    Identity = forms.CharField(max_length=100)
    VerificationCode = CaptchaField()

    class Meta:
        model = User
        fields = ('username','password1','password2','email','nickname','Identity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique':'该用户名已存在！' , 'invalid':'该用户名格式不符合要求！'}


