from secrets import choice
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.

class Department(models.Model):
    '''部门表'''
    # id = models.BigAutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=32, verbose_name='标题')

class UserInfo(models.Model):
    '''员工表'''
    gender_choices= (
        (1, '男'),
        (2, '女'),
    )
    name = models.CharField(max_length=16, verbose_name='姓名')
    password = models.CharField(max_length=64, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='账户余额')
    create_time = models.DateTimeField(verbose_name='入职时间')
    # depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    depart = models.ForeignKey(to='Department', to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')
