from django.shortcuts import render, redirect
from app02 import models
from app02.utils.pagination import Pagination
from app02.utils.form import *

def pretty_list(request):
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile='18188888888', price=10, level=1, status=1)

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['mobile__contains'] = search_data
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')
    print(queryset)
    page_object = Pagination(request, queryset)

    context = {
        'search_data':search_data, 
        'queryset':page_object.page_queryset, 
        'page_string': page_object.html()
        }

    return render (request, 'pretty_list.html', context)

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