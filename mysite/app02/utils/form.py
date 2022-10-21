from app02 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app02.utils.bootstrap import BootStrapModelForm

class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3, 
        label='用户名',
        widget=forms.TextInput(attrs={'class':'form-control'})
        )

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'create_time', 'gender', 'depart']

class PrettyModelForm(BootStrapModelForm):
    # 验证方式1
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = models.PrettyNum
        # fields = ['mobile', 'price', 'level', 'status']
        fields = '__all__'
        # exclude = ['level']

    # 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        exits = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exits:
            raise ValidationError('手机号已存在')
        # if len(txt_mobile) != 11:
            # raise ValidationError('格式错误')
        return txt_mobile

class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label='手机号')
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    # 验证方式1
    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = '__all__'
        # exclude = ['level']