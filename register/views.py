from django.shortcuts import render
from django.http.response import HttpResponseRedirect
# Create your views here.
def home(request):
    print(request.GET)
    return HttpResponseRedirect('index.html')

def accept(request):
    print("!")
    print(request.GET)
    return HttpResponseRedirect('index.html')   