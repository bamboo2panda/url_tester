from django.shortcuts import render

def index(request):
    return HttpResponse('Hello World!')
