from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import *

def home(request):
    return render(request, 'home.html')

@login_required()
def customer_page(request):
    return render(request, 'home.html')

@login_required()
def courier_page(request):
    return render(request, 'home.html')

def sign_up(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.username = email

            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'sign_up.html',{
        'form': form,
    })