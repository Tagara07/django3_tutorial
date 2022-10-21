

'''
自定义的分页组件
在视图函数中
    def pretty_list(request):
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
在html中
    {% for obj in queryset %}
        {{ obj.xx }}
    {% endfor %}
        
    <ul class="pagination">
        {{ page_string }}
    </ul>
'''
from django.utils.safestring import mark_safe
import copy

class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param='page', plus=5) -> None:
        
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True # 注释掉也可以
        self.query_dict = query_dict
        self.page_param = page_param
        
        page = request.GET.get(page_param, '1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = (page * page_size)

        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        if self.total_page_count <= 2*self.plus + 1:
            start_page = 1 
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2*self.plus
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2*self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(1)
        page_str_list.append(prev)

        for i in range(start_page, end_page+1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="/pretty/list/?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = '''
        <li>
            <form style="float: left; margin-left: -1px" method="get">
                <div class="input-group" style="width: 200px">
                    <input type="text" name="page" class="form-control" placeholder="页码">
                    <span class="input-group-btn">
                        <button class="btn btn-default" type="submit">跳转 </button>
                    </span>
                </div>
            </form>
        </li>
        '''

        page_str_list.append(search_string)

        page_string = mark_safe(''.join(page_str_list))
        return page_string