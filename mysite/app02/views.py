from django.shortcuts import render, redirect
from app02 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
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

def user_edit(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()
    
    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form':form})
    
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid:
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form':form})

def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')

def pretty_list(request):
    data_list = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_list['mobile__contains'] = search_data

    # res = models.PrettyNum.objects.filter(**data_list)
    # models.PrettyNum.objects.filter(mobile='', id='')
    queryset = models.PrettyNum.objects.filter(**data_list).order_by('-level')
    return render (request, 'pretty_list.html', {'queryset':queryset, 'search_data':search_data})

class PrettyModelForm(forms.ModelForm):
    # 验证方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = models.PrettyNum
        # fields = ['mobile', 'price', 'level', 'status']
        fields = '__all__'
        # exclude = ['level']

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class':'form-control', 'placeholder':field.label}
    
    # 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        exits = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exits:
            raise ValidationError('手机号已存在')
        # if len(txt_mobile) != 11:
            # raise ValidationError('格式错误')
        return txt_mobile

def pretty_add(request):
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {'form':form})

    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect('/pretty/list/')
    
    return render(request, 'pretty_add.html', {'form':form})

class PrettyEditModelForm(forms.ModelForm):
    # mobile = forms.CharField(disabled=True, label='手机号')
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    # 验证方式1
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = '__all__'
        # exclude = ['level']

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class':'form-control', 'placeholder':field.label}

def pretty_edit(request, nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    
    if request.method == 'GET':
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {'form':form})
    
    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid:
    #     # form.instance.字段名 = 值
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_edit.html', {'form':form})

def pretty_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')