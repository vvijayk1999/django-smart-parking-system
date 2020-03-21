from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create database
import sqlite3
import datetime

global conn
conn = sqlite3.connect('smart_parking_system.db',check_same_thread=False)
global c
c = conn.cursor()

try:
    c.execute('''CREATE TABLE users_vid (v_id text ,email text)''')
    print ("Table users_vid was created")
    conn.commit()
except:
    print("Table users_vid is already created")

def addusers_vidRecord(v_id,email):
    c.execute("INSERT INTO users_vid VALUES('"+v_id+"','"+email+"')")
    conn.commit()
##################


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            email = form.cleaned_data.get('email')
            v_id = form.cleaned_data.get('v_id')

            print('\n\n\n')
            print('email : '+email+'\nv_id :'+v_id)
            addusers_vidRecord(v_id,email)
            print('\n\n\n')

            messages.success(request, f'Account created for {email}')
            profile.save()
            return redirect('login')
    else:
        form = RegisterForm()    
    return render(request,'users/register.html',{'title': 'Register','form': form})

def login(request):
    return render(request,'users/login.html',{'title': 'Login'})