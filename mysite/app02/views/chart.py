from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    '''数据统计'''
    return render(request, 'chart_list.html')

def chart_bar(request):
    '''构造柱状图列表'''
    # 数据可以去数据库获取
    legend = ['猛男', '徐俊强']
    series_list = [
        {
            'name': '猛男',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
            },

            {
            'name': '徐俊强',
            'type': 'bar',
            'data': [50, 30, 36, 16, 10, 20]
            }
        ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        'status':True,
        'data':{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis
        }
    }
    return JsonResponse(result)