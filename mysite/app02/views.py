from pickletools import read_uint1
from turtle import title
from django.shortcuts import render, redirect
from app02 import models
# Create your views here.

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


def from_base(request):

    return render(request, 'from_base.html')

