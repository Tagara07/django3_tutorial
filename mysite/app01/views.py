from email import header
from urllib import request
from django.shortcuts import render, HttpResponse
import requests

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

def news(request):
    # headers = {'User-Agent':'这里放User-Agent'}
    res = requests.get('http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2017/10/news')
    data_list = res.json()
    print(data_list)
    return render(request, 'news.html', {'news_list': data_list})