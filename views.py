from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

def index(request):
    full_path = request.get_full_path().split('/')[2].split('_')
    print(full_path)
    server = 'tcp:127.0.0.1'
    database = 'reviews'
    username = 'sa'
    password = '6nY69p9ULm'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.close()
    with open("reviews.txt", "a") as f:
        f.write(full_path[0] + ':' + full_path[1] + '\n')
    return HttpResponse("<img src='image.jpg'>")
