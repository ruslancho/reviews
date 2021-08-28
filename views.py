from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h3>Привіт світ!</h3>")
