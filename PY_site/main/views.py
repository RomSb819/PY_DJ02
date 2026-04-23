from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def new(request):
    return render(request, "main/new.html")


def help_nature(request):
    return render(request, "main/help_nature.html")


def about(request):
    return render(request, "main/about.html")
