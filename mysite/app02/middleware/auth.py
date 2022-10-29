from django.utils.deprecation import MiddlewareMixin

class M1(MiddlewareMixin):
    '''中间件1'''

    def process_request(self, request):
        print('M1.进来了')

    def process_response(self, request, response):
        print('M1.走了')
        return response

class M2(MiddlewareMixin):
    '''中间件2'''

    def process_request(self, request):
        print('M2.进来了')

    def process_response(self, request, response):
        print('M2.走了')
        return response