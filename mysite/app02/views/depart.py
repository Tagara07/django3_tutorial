from django.shortcuts import render, redirect
from app02 import models
from app02.utils.pagination import Pagination
from app02.utils.form import *

def depart_list(request):
    '''部门列表'''

    info = request.session.get('info')
    if not info:
        return redirect('/login/')

    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset':queryset})

def depart_add(request):

    info = request.session.get('info')
    if not info:
        return redirect('/login/')

    if request.method == 'GET':
        return render(request, 'depart_add.html')
    
    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    return redirect('/depart/list/')

def depart_delete(request):

    info = request.session.get('info')
    if not info:
        return redirect('/login/')

    nid = request.GET.get('nid')
    print(nid)
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')

def depart_edit(request, nid):

    info = request.session.get('info')
    if not info:
        return redirect('/login/')
        
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        # print(row_object.id, row_object.title)
        return render(request, 'depart_edit.html', {'row_object':row_object})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    # models.Department.objects.filter(id=nid).update(title=title, 其他='123')
    return redirect('/depart/list/')