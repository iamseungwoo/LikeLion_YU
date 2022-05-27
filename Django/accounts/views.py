from django.shortcuts import redirect, render
from django.contrib import auth

def login(request):
    if request.method == "POST":
        user_id = request.POST['Username']
        pwd = request.POST['Password']
        user = auth.authenticate(request, username=user_id, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    return



