#created by shrikant
from django.http.response import HttpResponse
from django.shortcuts import render
from http import HTTPStatus
# Create your views here.
def indexx(request):
    return HttpResponse("index of blogging  urls")
def ind(request):
    return HttpResponse('''ind of blogging  urls<a href='https://docs.djangoproject.com/en/3.2/intro/tutorial01/'>django create app</a><br>
    ''')
def ind2(request):
    return HttpResponse('''ind2 of blogging  urls<a href='https://docs.djangoproject.com/en/3.2/intro/tutorial01/'>django create app</a><br>
    ''')