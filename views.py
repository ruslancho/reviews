from django.shortcuts import render
from django.http import HttpResponse
import pyodbc

def index(request):
    full_path = request.get_full_path().split('/')[2].split('_')
    print(full_path)
    with open("reviews.txt", "a") as f:
        f.write(full_path[0] + ':' + full_path[1] + '\n')
    server = 'tcp:192.168.102.33'
    database = 'reviews'
    username = 'sa'
    password = '6nY69p9ULm'


    with pyodbc.connect('DRIVER='+'{ODBC Driver 17 for SQL Server}'+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO reviews (request_number ,rating) VALUES ('IR10055', '5')")
    return HttpResponse("<img src='https://www.imgonline.com.ua/examples/bee-on-daisy.jpg'>")
