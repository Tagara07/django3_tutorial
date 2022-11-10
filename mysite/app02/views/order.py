import random
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app02 import models
from app02.utils.bootstrap import BootStrapModelForm

class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = '__all__'
        exclude = ['oid']

def order_list(request):
    form = OrderModelForm()
    return render(request, 'order_list.html', {'form': form})

@csrf_exempt
def order_add(request):
    '''新建订单（Ajax请求）'''
    form = OrderModelForm(data=request.POST)

    if form.is_valid():
        # 随机生成oid
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        form.save()
        return JsonResponse({"status": True})

    return JsonResponse({"status":False, 'error':form.errors})