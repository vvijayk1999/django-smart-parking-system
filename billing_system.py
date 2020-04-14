import paho.mqtt.client as mqtt
import sqlite3
from pyfcm import FCMNotification
import json
from datetime import date, datetime
import time

#----------------------------------------------------------------------

push_service = FCMNotification(api_key="AAAAj7P1O5g:APA91bHUCdu3Pf3pdewj2co-rQO9yFwkWjTm2FKbvHNrMZwrWw6KZ2OUDy_sdilVTXTdBg7KqWh6EH3rt6P34CXNpYrdgSC3eJMPjY-iwx_a5rXXmPCCCUITurpYLpl-Kfe2rz2oNHBn")

broker_address= "35.225.7.175"
port = 1883 #portNumber
#user = "<username>"
#password = "<password>"
topic = "getSlotDetails"
#----------------------------------------------------------------------

def billing_system():
    connect()
    client = mqtt.Client('as6g54er6has4')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address,port, 60)
    #client.on_log=on_log
    client.loop_forever()

def connect():
    global conn
    conn = sqlite3.connect('smart_parking_system.db')
    global c
    c = conn.cursor()
    
def Values(message):
    print(message)
    parsed_json = (json.loads(message))
    Topic=(parsed_json['topic'])
    if(Topic=="slot_details"):
        v_id=(parsed_json['number_plate'])
        model=(parsed_json['brand'])
        arrival_time=(parsed_json['entry_time'])
        departure_time=(parsed_json['exit_time'])
        slot_no=(parsed_json['slot_number'])
        place=(parsed_json['place_name'])
        current_date = str(date.today())

        FMT = '%H:%M:%S'

        duration = datetime.strptime(departure_time , FMT) - datetime.strptime(arrival_time , FMT)
        hours = time.strptime(str(duration), FMT)
        x=hours.tm_hour
        if x==1:
            amount = str(30)
        elif x>=2:
            amount=str(int(30)+x*int(10))
        print(v_id,model,arrival_time,departure_time,slot_no,place,current_date,amount)
        
        #c.execute("INSERT INTO Data VALUES('"+v_id+"','"+model+"','"+arrival_time+"','"+departure_time+"','"+slot_no+"','"+place+"','"+current_date+"','"+amount+"')")
        c.execute("INSERT INTO History VALUES('"+v_id+"','"+model+"','"+arrival_time+"','"+departure_time+"','"+str(slot_no)+"','"+place+"','"+current_date+"','"+amount+"')")

        message_string = "Your vehicle with number "+v_id+" was parked at "+place+" from "+arrival_time+" to "+departure_time+" on "+current_date+". \nYou have been charged Rs."+amount

        sendPushNotifications(v_id,message_string)

        print("row inserted")
        c.execute("UPDATE Slots SET status = '0' WHERE slot_num = '"+slot_no+"' and place='"+place+"'")
        print("row updated") 
    elif(Topic=="slot_status"):
        slot_num=(parsed_json['slot_number'])
        status=(parsed_json['occupancy'])
        place=(parsed_json['place_name'])
        print(slot_num,status)
        c.execute("INSERT INTO Slots VALUES('"+slot_num+"','"+status+"','"+place+"')")
        print("row inserted")  
    conn.commit()
          
def CloseConnection():
    conn.close()

def on_connect(client, userdata, flags, rc):
    print("Connected with code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    message=str(msg.payload.decode("utf-8"))
    print(message)
    Values(message)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def sendPushNotifications(v_id,message_string):

    try:
        c.execute("SELECT email FROM users_vid WHERE v_id = '%s'" %v_id)
        result=c.fetchall()
        for row in result:

            topic = row[0].split('@')[0]+'%'+row[0].split('@')[1]

            message_title = "Billing was successfull !"
            result = push_service.notify_topic_subscribers(topic_name=topic, message_body=message_string,message_title=message_title)
    except:
        pass
    
