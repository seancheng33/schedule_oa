from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from util.encryption_string import md5_encrypt
from usercenter import models


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号',
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$','手机号格式错误'),])
    password = forms.CharField(label='密码',
                               min_length=8,
                               max_length=64,
                               error_messages={
                                   "min_length":"密码长度不能小于8个字符",
                                   "max_length":"密码长度不能大于64个字符"
                               },
                               widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())

    code = CaptchaField(label='验证码')

    class Meta:
        model = models.UserInfo
        fields = ["username","email","password","confirm_password","mobile_phone","code"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' %(field.label)


    def clean_username(self):
        username = self.cleaned_data['username']
        exsits = models.UserInfo.objects.filter(username=username).exists()
        if exsits:
            raise ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        exsits = models.UserInfo.objects.filter(email=email).exists()
        if exsits:
            raise ValidationError('邮件已存在')
        return email

    def mobile_phone(self):
        mobile_phone = self.cleaned_data['mobile_phone']
        exsits = models.UserInfo.objects.filter(mobile_phone=mobile_phone).exists()

        print(RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$'))

        if exsits:
            raise ValidationError('手机号已存在')
        return mobile_phone

    def clean_confirm_password(self):
        pwd = self.cleaned_data['password']
        confirm_pwd = self.cleaned_data['confirm_password']
        if pwd != confirm_pwd:
            raise ValidationError('两次输入密码不一致')

        return confirm_pwd

class LoginForm(BaseException,forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    code = CaptchaField(label='验证码')