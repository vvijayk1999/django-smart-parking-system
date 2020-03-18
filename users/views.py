from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')
            profile.save()
            return redirect('login')
    else:
        form = RegisterForm()    
    return render(request,'users/register.html',{'title': 'Register','form': form})

def login(request):
    return render(request,'users/login.html',{'title': 'Login'})