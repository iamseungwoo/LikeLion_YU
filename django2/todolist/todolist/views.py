from django.shortcuts import render

def home(request) :
    return render(request, 'home.html')

def calender(request) :
    return render(request, 'calender.html')