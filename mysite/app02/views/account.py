from hashlib import md5
from django.shortcuts import render, redirect, HttpResponse
from django import forms

from app02 import models
from app02.utils.bootstrap import BootStrapForm
from app02.utils.encrypt import md5

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label='用户名', 
        widget=forms.TextInput,
        required=True
        )
    password = forms.CharField(
        label='密码', 
        widget=forms.PasswordInput(render_value=True),
        required=True
        )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


def login(request):
    '''登录'''
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form':form})
        
        # 用户名和密码正确
        request.session['info'] = {'id':admin_object.id, 'name':admin_object.username}
        return redirect('/admin/list/')
    return render(request, 'login.html', {'form':form})
    


