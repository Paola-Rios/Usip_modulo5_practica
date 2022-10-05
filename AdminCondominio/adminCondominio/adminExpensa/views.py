from django.shortcuts import render
from django.http import HttpResponse

# function view 
def index (request):
    return HttpResponse("hola mundo")
