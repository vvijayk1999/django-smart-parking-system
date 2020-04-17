from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ParkingCards, Slots, Places

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
        
        _ = Places()
        _.latitude = "12.991734"
        _.longitude = "77.571458"
        _.value = 'mantri-mall'
        _.name = 'Mantri Mall'

        #places = ['Mantri Mall','REVA University','Fun World','Manyata Tech Park']
        places = [_]

        return render(request,'home/dashboard.html',{'title': 'Dashboard','parkingCards': parkingCards,'places':places})

def about(request):
    return render(request,'home/about.html',{'title': 'About'})
    
@login_required
def reserve(request):
    _ = Places()
    _.latitude = "12.991734"
    _.longitude = "77.571458"
    _.value = 'mantri-mall'
    _.name = 'Mantri Mall'

    #places = ['Mantri Mall','REVA University','Fun World','Manyata Tech Park']
    places = [_]
    return render(request,'home/reserve.html',{'title':'Book a slot','places':places})

month = date.today().strftime("%b")
year = date.today().strftime("%Y")
date = date.today().strftime("%d")

current_date = month + ' ' + date + ', '+year

def slotInfo(request):
        
    place = request.GET['place']
    date = request.GET['date']

#Apr 17, 2020
    body = ''
    c.execute("SELECT * FROM Online_slots WHERE place ='%s'" %(place))
    #c.execute("SELECT * FROM Online_slots ")
    result=c.fetchall()
    print(result)

    for row in result:
        bg_color = '#0F0'       #
        text_color = '#000'     #   Defaults
        message = 'Available'   #
        border = ''

        if row[1] == "0":   #   Available
            bg_color = '#FFF'#  White
            text_color = '#000'#Black 
            message = 'Available'
            border = 'border-style: solid;'   
        if row[1] == "2":   #   Reserved
            bg_color = "#ffa500"#Orange
            text_color = "#000"#Black
            message = "Reserved"

        number = row[0]
        div = '<div class="slot" style="background-color: '+bg_color+'; '+border+' "><h2 style="color: '+text_color+';">'+str(number)+'</h2><br><h5 style="color:'+text_color+';">'+message+'</h5></div>'
        body+=div

    if place == '':
        body = '<h4>Please select a place.</h4>'    

    html = '<div class="slots-info">'+body+'</div>'

    return HttpResponse(html)

def realtimeSlotInfo(request):

    place = request.GET['place']

    body = ''
    c.execute("SELECT * FROM RealtimeSlots WHERE place='"+place+"'")
    result=c.fetchall()
    for row in result:
        bg_color = '#0F0'       #
        text_color = '#000'     #   Defaults
        message = 'Available'   #

        if row[1] == "0":   #   Available
            bg_color = '#46cf46'#  Green
            text_color = '#000'#Black 
            message = 'Available'   
        if row[1] == "1":   #   Occupied
            bg_color = "#eb2f2f"#  Red
            text_color = "#FFF"#White
            message = "Occupied"
        if row[1] == "2":   #   Reserved
            bg_color = "#ffa500"#Orange
            text_color = "#000"#Black
            message = "Reserved"

        number = row[0]
        div = '<div class="realtime-slot" style="background-color: '+bg_color+'; "><h2 style="color: '+text_color+';">'+str(number)+'</h2><br><h5 style="color:'+text_color+';">'+message+'</h5></div>'
        body+=div

    if place == '':
        body = '<h4>Please select a place.</h4>'    

    html = '<div class="slots-info">'+body+'</div>'

    return HttpResponse(html)