from django.http.response import HttpResponse
from django.shortcuts import render
from http import HTTPStatus
# Create your views here.
def index(request):
    return render(request,'hh.html')
def ind(request):
    return HttpResponse("ind of home urls")