from django.shortcuts import render

def login(request):
    return


def logout(request):
    return

def signup(request):
    return



from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

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
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')



