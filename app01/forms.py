from django import forms
from django.forms import widgets
from django.core.validators import ValidationError

class RegForm(forms.Form):
    username = forms.CharField(label='用户名a',
                               min_length=6,
                               error_messages={
                                   'min_length': '不能少于6位',
                                   'required': '不能为空'
                               }
                               )
    password = forms.CharField(label='密码',
                               min_length=6,
                               widget=widgets.PasswordInput()
                               )
    re_password = forms.CharField(label='确认密码',
                                  min_length=6,
                                  widget=widgets.PasswordInput()
                                  )
    department = forms.ChoiceField(label='部门')


    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_password','两次密码不一致')
        raise ValidationError('两次密码不一致')