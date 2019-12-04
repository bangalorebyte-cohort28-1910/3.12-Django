# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, This is from polls app")

def about(request):
    return HttpResponse("This is About Page")