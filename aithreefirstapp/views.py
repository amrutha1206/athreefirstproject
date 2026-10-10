from django.shortcuts import render

# Create your views here.

def sample(request):
    return HttpResponse("<h1><center>Hello World!!!</center></h1>")