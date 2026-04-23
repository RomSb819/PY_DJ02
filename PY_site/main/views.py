from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'caption': "Берегите природу"})

def new(request):
    return render(request, 'main/new.html')
