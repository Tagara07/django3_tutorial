from urllib import request
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    return render(request, 'user_list.html')

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