from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

class 自定义登录表单(AuthenticationForm):
    验证码 = CaptchaField()

class 自定义编辑表单(UserChangeForm):
    昵称 = forms.CharField(required=False,max_length=50)
    身份 = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','password','email','昵称','身份')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique':'该用户名已存在！' , 'invalid':'该用户名格式不符合要求！'}


class 自定义注册表单(UserCreationForm):
    昵称 = forms.CharField(required=False,max_length=50)
    身份 = forms.CharField(max_length=100)
    验证码 = CaptchaField()

    class Meta:
        model = User
        fields = ('username','password1','password2','email','昵称','身份')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique':'该用户名已存在！' , 'invalid':'该用户名格式不符合要求！'}


