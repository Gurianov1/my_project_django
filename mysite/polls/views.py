from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return HttpResponse("My name is Egor")

def contacts(request):
    return HttpResponse("My  contacts")

def hobbies(request):
    return HttpResponse("My hobbies")

def gallery(request):
    return HttpResponse("My ngallery")
