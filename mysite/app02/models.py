from django.db import models

# Create your models here.

class Admin(models.Model):
    '''管理员'''
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=64, verbose_name='密码')

    def __str__(self):
        return self.username

class Department(models.Model):
    '''部门表'''
    # id = models.BigAutoField(primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=32, verbose_name='标题')

    def __str__(self) -> str:
        return self.title

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
    # create_time = models.DateTimeField(verbose_name='入职时间')
    create_time = models.DateField(verbose_name='入职时间')
    # depart = models.ForeignKey(to='Department', to_field='id', on_delete=models.CASCADE)
    depart = models.ForeignKey(to='Department', to_field='id', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='部门')
    gender = models.SmallIntegerField(choices=gender_choices, verbose_name='性别')

class PrettyNum(models.Model):
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    price = models.IntegerField(verbose_name='价格')
    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
        (4, '4级'),
    )
    level = models.SmallIntegerField(choices=level_choices, default=1, verbose_name='级别')

    status_choices = (
        (1, '已占用'),
        (2, '未占用'),
    )
    status = models.SmallIntegerField(choices=status_choices, default=2, verbose_name='状态')

class Task(models.Model):
    '''任务'''
    level_choice = (
        (1, '紧急'),
        (2, '重要'),
        (3, '临时')
    )
    level = models.SmallIntegerField(choices=level_choice, default=1, verbose_name='级别')
    title = models.CharField(max_length=64, verbose_name='标题')
    detail = models.TextField(verbose_name='详细信息')
    user = models.ForeignKey(to='Admin', to_field='id', on_delete=models.CASCADE, verbose_name='负责人')

class Order(models.Model):
    '''工单'''
    oid = models.CharField(max_length=64, verbose_name="订单号")
    title = models.CharField(max_length=32, verbose_name="名称")
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, '待支付'),
        (2, '已支付'),
    )
    status = models.SmallIntegerField(choices=status_choices, default=1, verbose_name='状态')

    admin = models.ForeignKey(to='Admin', on_delete=models.CASCADE, verbose_name="管理员")
    

