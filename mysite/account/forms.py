from django import forms

from django.contrib.auth.models import User #Django默认的用户数据模型，即auth_user
from .models import UserProfile
#数据类模型:forms.Form类，提交表单之后，不会对数据进行修改。forms.ModelForm，将表单中的数据写入数据库表或者修改某些记录的值。


#实现登录功能
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


#实现注册功能(不单独创建数据库，利用原有的数据库，即Django默认的用户数据模型)
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    #内部类（声明本表单类所应用的数据模型，也就是将来表单的内容会写入哪个数据库表中的哪些记录里面。username与email写入auth_user表中）：
    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data  #cleaned_data是实例的属性，它以字典形式返回实例的具体数据
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']


#phone与birth写入account_userprofile表中
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")