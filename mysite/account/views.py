from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm,  RegistrationForm,  UserProfileForm

#在视图函数中要处理前端提交的数据，并支持前端的显示请求，视图函数必须使用request作为第一个函数。request:Httprequest
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Welcome you.You have been authenticate successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()  #创建了LoginForm类的实例login_form，但没有向类中传递任何参数，这个实例称为未绑定实例。
        return render(request, "account/login.html", {"form": login_form}) #form被传到login.html


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        #ModelForm类或者它的子类都具有save()方法，它的效果是将表单数据保存到数据库，并生成该数据对象
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False) #commit=False：数据并没有被保存到数据库，仅生成一个数据对象new_user
            new_user.set_password(user_form.cleaned_data['password']) #设置该数据对象new_user的密码
            new_user.save() #密码已经保存到数据对象new_user中，再执行new_user.save()就可以把数据保存到数据库中

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user  #将new_user数据赋值给数据对象new_profile
            new_profile.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry,you can't register.")
    else:
        user_form = RegistrationForm()

        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile":userprofile_form}) #"form"与"profile"被传到register.html
