from captcha.fields import CaptchaField
from django.shortcuts import render
from django import forms
from usercenter import models
from django.core.validators import RegexValidator
from django_redis import get_redis_connection

# Create your views here.
def index():
    conn = get_redis_connection()

    pass


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$','手机号格式错误'),])
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())

    code = CaptchaField(label='验证码')

    class Meta:
        model = models.UserInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' %(field.label)

def register(request):
    if request.POST:
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            print('success')
            pass
    else:
        form = RegisterModelForm()

    return render(request,'register.html',{'form':form})
