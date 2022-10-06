from urllib import request
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    return render(request, 'user_list.html')

def user_add(request):
    return render(request, 'user_add.html')

def tpl(request):
    return render(request, 'tpl.html')