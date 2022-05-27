#models.py
from django.db import models

class Apply(models.Model):
    name = models.CharField(max_length=10)
    id = models.IntegerField()
    ans1 = models.CharField(max_length=10)
    ans2 = models.TextField()
    ans3 = models.TextField()
    ans4 = models.TextField()
    ans5 = models.TextField()

from django.contrib import admin
from .models import Apply

admin.site.register(Apply.name)

models.py 작성후 명령어 : python manage.py makemigrations

#views.py
from django.contrib import auth
from .forms import ApplyForm
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def apply(request): # 지원서 html
    return render(request, 'apply.html')

def create(request):
    if(request.method == 'POST'):
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplyForm()
    return render(request, 'apply.html')

# forms.py
from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):
	class Meta:
        model = Apply
        fields = '__all__'


	

	