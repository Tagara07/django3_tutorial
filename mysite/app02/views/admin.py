from contextlib import redirect_stderr
from genericpath import exists
from pyexpat import model
from tkinter import Widget
from django.shortcuts import render, redirect
from django import forms

from app02 import models
from django.core.exceptions import ValidationError

from app02.utils.pagination import Pagination
from app02.utils.bootstrap import BootStrapModelForm
from app02.utils.encrypt import md5


def admin_list(request):
    # 构造搜索

    # 检查用户是否登录
    info = request.session.get('info')
    if not info:
        return redirect('/login/')
    print(info)

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['username__contains'] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)

    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'queryset':page_object.page_queryset,
        'page_string':page_object.html(),
        'search_data':search_data
    }
    return render(request, 'admin_list.html', context)

class AdminModelForm(BootStrapModelForm):

    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)
        )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致，请重新输入')
        return confirm

class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']

class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)
        )
    
    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)

        models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('不能与以前的密码相同 ')
        return md5_pwd

    def clean_confirm_password(self):
        # print(self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致，请重新输入')
        return confirm

def admin_add(request):
    """添加管理员"""
    title = '新建管理员'
    
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {'form':form, 'title':title})
    
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')  

    return render(request, 'change.html', {'form':form, 'title':title})


def admin_edit(request, nid):
    '''编辑管理员'''

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {'msg':'数据不存在'})

    title = '编辑管理员'
    if request.method == 'GET':
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', {'form':form, 'title':title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'form':form, 'title':title})

def admin_delete(request, nid):
    '''删除管理员'''
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list')

def admin_reset(request, nid):
    '''重置密码'''
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')

    title = '重置密码 - {}'.format(row_object.username)

    if request.method == 'GET':
        form = AdminResetModelForm()
        return render(request, 'change.html', {'form':form, 'title': title}) 

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {'form':form, 'title':title})