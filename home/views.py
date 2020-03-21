from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ParkingCards

from billing_system import *
import multiprocessing as mp


# Create your views here.
import sqlite3
import datetime

global conn
conn = sqlite3.connect('smart_parking_system.db',check_same_thread=False)
global c
c = conn.cursor()

try:
    c.execute('''CREATE TABLE History
         (v_id text,model text,arrival_time text,departure_time text,slot_no text,place text,current_date text,amount text)''')
    print ("table History done")
    conn.commit()
except:
    print("Table History is already created")

#################################################################
p1 = mp.Process(target=billing_system)
p1.start()
print('\nBilling sytem process is running . . .\n')
#################################################################

@login_required
def dashboard(request):
    if request.method == "POST":
        pass
    else:
        c.execute("SELECT * FROM History WHERE v_id = '%s'" %request.user.get_v_id())
        result=c.fetchall()
        items = []
        for row in result:
            items.append(row)        
        parkingCards = []
        for i in items:
            _ = ParkingCards()
            _.place = i[-3]
            _.arrival_time = i[2]
            _.departure_time = i[3]
            _.date = i[-2]
            _.price = i[-1]
            parkingCards.append(_)
        return render(request,'home/dashboard.html',{'title': 'Dashboard','parkingCards': parkingCards})

def main(request):
    return render(request,'home/index.html',{'title': 'Smart Parking System'})