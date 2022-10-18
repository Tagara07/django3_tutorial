from dataclasses import fields
from tkinter import Widget
from django.shortcuts import render, redirect
from app02 import models
from django import forms

# Create your views here.

def from_base(request):

    return render(request, 'from_base.html')

def depart_list(request):
    '''部门列表'''
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset':queryset})

def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    
    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/depart/list/')

def depart_delete(request):
    nid = request.GET.get('nid')
    print(nid)
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')

def depart_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id, row_object.title)
        return render(request, 'depart_edit.html', {'row_object':row_object})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    # models.Department.objects.filter(id=nid).update(title=title, 其他='123')
    return redirect('/depart/list/')

def user_list(request):
    return render(request, 'user_list.html')

def user_list(request):
    queryset = models.UserInfo.objects.all() 
    # for obj in queryset:
        # print(obj.id, obj.name, obj.create_time.strftime('%Y-%m-%d'), obj.get_gender_display(), obj.depart.title)
    return render(request, 'user_list.html', {'queryset':queryset})

def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        } 
        return render(request, 'user_add.html', context)

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    models.UserInfo.objects.create(name=user, password=pwd, age=age, 
                                account=account, create_time=ctime, gender=gender, 
                                depart_id=depart_id)

    return redirect('/user/list/')

class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=3, label='用户名')
    # password = forms.CharField(min_length=3, label='密码', validators=)
    
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'create_time', 'gender', 'depart']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control'}),
        #     'password': forms.TextInput(attrs={'class':'form-control'}),
        #     'age': forms.TextInput(attrs={'class':'form-control'}),
        # }
    
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        for name, field in self.fields.items():
            # if name == 'password':
                # continue
            field.widget.attrs = {'class':'form-control', 'placeholder':field.label}


def user_model_form_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form':form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')
    
    return render(request, 'user_model_form_add.html', {'form':form})