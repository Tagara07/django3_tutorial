from django.shortcuts import render
from app02 import models
# Create your views here.

def depart_list(request):
    '''部门列表'''
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset':queryset})

def depart_add(request):
    return render(request, 'depart_add.html')

def from_base(request):

    return render(request, 'from_base.html')

