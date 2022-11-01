from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

class AuthMiddleware(MiddlewareMixin):
 
    def process_request(self, request):
        # 0.排除那些不需要登陆就能访问的页面
        if request.path_info in ['/login/', '/image/code/']:
            return

        info_dict = request.session.get('info')
        if info_dict:
            return

        # 没有登陆过，重新回到登录页面
        return redirect('/login/')