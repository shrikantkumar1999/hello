#created by shrikant
from django.http.response import HttpResponse
from django.shortcuts import render
from http import HTTPStatus
# Create your views here.
def indexx(request):
    return HttpResponse("index of blogging  urls")
def ind(request):
    return HttpResponse("ind of blogging  urls")