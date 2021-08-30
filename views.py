from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    full_path = request.get_full_path().split('/')[2].split('_')
    print(full_path)
    with open("reviews.txt", "a") as f:
        f.write(full_path[0] + ':' + full_path[1] + '\n')
    return HttpResponse("<img src='image.jpg'>")
