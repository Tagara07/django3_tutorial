from urllib import request
from django.shortcuts import render, HttpResponse, redirect

from app01.models import *

# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')

def user_list01(request):
    return render(request, 'user_list01.html')

def user_add(request):
    return render(request, 'user_add.html')

def tpl(request):
    name = '韩朝'
    roles = ['管理员', 'CEO', '保安']
    user_info = {'name':'郭志', 'salary':10000, 'role': 'CTO'}

    date_list = [
        {'name':'郭志', 'salary':10000, 'role': 'CTO'},
        {'name':'卢辉', 'salary':10000, 'role': 'CTO'},
        {'name':'召见先', 'salary':10000, 'role': 'CTO'}    
    ]

    return render(request, 'tpl.html', {
                                        "n1": name, 
                                        'n2': roles, 
                                        'n3': user_info,
                                        'n4': date_list
                                        })


def something(request):
    print(request.method)
    print(request.GET)
    # return HttpResponse('返回内容')
    # return render(request, 'something.html', {'title': '来了'})
    return redirect('https://baidu.com')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # print(request.POST)
    username = request.POST.get('user')
    password = request.POST.get('pwd')

    if username == 'root' and password == '123':
        # return HttpResponse('登录成功')
        return redirect('https://share.dmhy.org/')
 
    # return HttpResponse('登录失败')
    return render(request, 'login.html', {'error_msg':'用户名或密码错误'})

def orm(request):
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='IT部')
    # Department.objects.create(title='运营部')

    # UserInfo.objects.create(name='mengnan', password='123', age='19', size=10)
    # UserInfo.objects.create(name='xiaopang', password='666', age='29', size=15  )

    # UserInfo.objects.filter(id=2).delete()
    # Department.objects.all().delete()

    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)

    UserInfo.objects.all().update(password=999)
    UserInfo.objects.filter(name='mengnan').update(password=99)
    return HttpResponse('成功')


def info_list(request):

    data_list = UserInfo.objects.all()
    # print(data_list)

    return render(request, 'info_list.html', {'data_list':data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    size = request.POST.get('size')

    UserInfo.objects.create(name=user, password=pwd, age=age, size=size)

    # return HttpResponse('添加成功')
    return redirect('/info/list')

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    # return HttpResponse('删除成功')
    return redirect('/info/list')
