from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def addition(request):
    return render(request, 'home.html',{'name':'Rohit'})

def add(request):
    val1= float(request.GET["num1"])
    val2= float(request.GET["num2"])

    Res = val1 + val2

    return render(request, 'result.html', {'result': Res})
