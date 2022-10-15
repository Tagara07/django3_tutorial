"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views as views01
from app02 import views as views02

urlpatterns = [
    # path('admin/', admin.site.urls), 
    path('index/', views01.index), 
    path('user/list01/', views01.user_list01), 
    path('user/add/', views01.user_add),
    path('tpl/', views01.tpl),
    # path('news/', views.news),
    path('something/', views01.something),
    path('login/', views01.login),
    path('orm/', views01.orm),
    path('info/list/', views01.info_list),
    path('info/add/', views01.info_add),
    path('info/delete/', views01.info_delete),
    path('depart/list/', views02.depart_list),
    path('depart/add/', views02.depart_add),
    path('depart/delete/', views02.depart_delete),
    path('depart/<int:nid>/edit/', views02.depart_edit),
    path('user/list/', views02.user_list),
    path('from_base/', views02.from_base),
]
