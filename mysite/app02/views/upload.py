from django.shortcuts import render, HttpResponse

def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')

    # print(request.POST) # 请求体中数据
    # print(request.FILES) # 请求发来的文件
    file_object = request.FILES.get('avatar')
    print(file_object.name)
    
    f = open(file_object.name, mode='wb')
    for chunck in file_object.chunks():
        f.write(chunck)
    f.close()
    return HttpResponse('....')