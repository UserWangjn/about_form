from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import widgets
from app01.forms import RegForm




def register(request):
    form_obj = RegForm()

    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            print(form_obj.cleaned_data)
            return HttpResponse('okkk')
    return render(request, 'reg.html', {'form_obj': form_obj})
