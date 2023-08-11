from django.http import HttpResponse
from django.shortcuts import render

def  inicio(request):
    http_response = render(request=request, template_name='inicio.html', context={},)
    return http_response

def  acerca(request):
    http_response = render(request=request, template_name='acerca.html', context={},)
    return http_response

def  statics(request):
    http_response = render(request=request, template_name='statics.html', context={},)
    return http_response