from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import time
from datetime import date
import random

from pyfcm import FCMNotification
import sqlite3

# Create your views here.
import sqlite3
import datetime

push_service = FCMNotification(api_key="AAAAj7P1O5g:APA91bHUCdu3Pf3pdewj2co-rQO9yFwkWjTm2FKbvHNrMZwrWw6KZ2OUDy_sdilVTXTdBg7KqWh6EH3rt6P34CXNpYrdgSC3eJMPjY-iwx_a5rXXmPCCCUITurpYLpl-Kfe2rz2oNHBn")

global conn
conn = sqlite3.connect('smart_parking_system.db',check_same_thread=False)
global c
c = conn.cursor()

try:
    c.execute('''CREATE TABLE Booking
            (v_id text PRIMARY KEY,b_time text,duration text,s_no int,place text,b_date text)''')
    c.execute('''CREATE TABLE Online_slots
         (slot_num int,status text,place text,current_date text,PRIMARY KEY(slot_num,place))''')
    print ("table Booking created")
    conn.commit()
except:
    print("Table Booking is already created")

def convert12to24(time):
    timeList = time.split(' ')
    hours = timeList[0].split(':')[0]
    mins = timeList[0].split(':')[1]
    am_pm = timeList[1]
    if am_pm == 'AM' and hours == '12':
        return '00' +':'+ mins
    elif am_pm == 'AM':
        return hours +':'+ mins
    elif am_pm == 'PM' and hours == '12':
        return hours +':'+ mins
    else:
        return str(int(hours)+12) +':'+ mins

def convertDate(date):  #Apr 07, 2021
    year = date.split(', ')[1]
    month = date.split(' ')[0]
    day = date.split(' ')[1].split(', ')[0]

s_no = ''
current_date = date.today()

def DBrequest(b_time,duration,place,b_date):
    global s_no
    if(b_date!=current_date):
        s_no= c.execute("SELECT slot_num FROM Online_slots WHERE status = '0' AND current_date ='"+b_date+"' AND place = '"+place+"' ORDER BY RANDOM() LIMIT 1")
    else:
        s_no=random.randrange(1,5,1) 
    FMT = '%H:%M'
    hours = time.strptime(str(duration), FMT)
    minutes = time.strptime(str(duration), FMT)
    x=hours.tm_hour
    y=minutes.tm_min
    if (x==1 or x < 1 and y > 0):
        amount = str(30)
    elif x>=2:
        amount=str(int(30)+(x-1)*int(10))
    print(amount)

    if s_no == '':
        return False
    else:
        return 'Parking space is available at '+place+' on '+b_date+' , '+b_time+' and you will be charged Rs.'+amount+'\nWould you like to proceed ?'


    #acknowledge (confirm booking?)
def proceedToBooking(v_id,b_time,duration,place,b_date,email):

    global s_no

    c.execute("INSERT INTO Booking VALUES('"+v_id+"','"+b_time+"','"+duration+"','"+s_no+"','"+place+"','"+b_date+"')")
    print("row inserted")


    #########################  Push Notifications  ########################################

    message_string = 'Hello there,\nYour pre-booking reservation was successfull!\n\nInfo:\nVehicle number:'+v_id

    topic = email[0].split('@')[0]+'%'+email[0].split('@')[1]
    print(topic)
    message_title = "Smart Parking System"
    result = push_service.notify_topic_subscribers(topic_name=topic, message_body=message_string,message_title=message_title)
    #######################################################################################


    status=2
    c.execute("SELECT * FROM Online_slots WHERE slot_num= '%s' AND place = '%s'" %(s_no,place))
    if c.fetchall():
        c.execute("UPDATE Online_slots SET status = '2' WHERE slot_num = '+s_no+' and place='+place+' and current_date = '+date' ")
    else:
        c.execute("INSERT INTO Online_slots VALUES('"+s_no+"','"+status+"','"+place+"','"+current_date+"')")
        print("row inserted")

# Create your views here.

@login_required              
def bookSlots(request):
    if request.method == "GET":
        #print("-------- BOOKED -----------")

        time = convert12to24(request.GET['time'])
        date = request.GET['date']
        duration = request.GET['duration']
        place = request.GET['place']

        email = request.GET['email']
        v_id = request.GET['v_id']

        proceedToBooking(v_id,time,duration,place,date,email)
        return HttpResponse('True')

@login_required
def checkSlots(request):
    if request.method == "GET":

        slot_available_staus = False
        #    try:
        time = convert12to24(request.GET['time'])
        date = request.GET['date']
        duration = request.GET['duration']
        place = request.GET['place']

        #   Logging
        print(time)
        print(date)
        print(duration)
        print(place)

        staus = DBrequest(time,duration,place,date)

        if staus == False:
            return HttpResponse(staus)
        else:
            return HttpResponse(staus)
    #except:
        slot_available_staus = False
        print('ERROR : Missing Values')
        return HttpResponse(str(slot_available_staus))
    