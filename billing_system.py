import paho.mqtt.client as mqtt
import sqlite3
import json
from datetime import date, datetime
import time

#----------------------------------------------------------------------
broker_address= "34.93.196.242"
port = 1883 #portNumber
#user = "<username>"
#password = "<password>"
topic = "getSlotDetails"
#----------------------------------------------------------------------

def billing_system():
    connect()
    client = mqtt.Client('parkingsystem')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address,port, 60)
    client.on_log=on_log
    client.loop_forever()

def connect():
    global conn
    conn = sqlite3.connect('smart_parking_system.db')
    global c
    c = conn.cursor()
    
def Values(message):
    parsed_json = (json.loads(message))
    print(parsed_json)

    v_id = parsed_json[0]['number_plate']
    model = parsed_json[0]['brand']
    arrival_time = parsed_json[0]['entry_time']
    departure_time = parsed_json[0]['exit_time']
    slot_no = parsed_json[0]['slot_number']
    place = parsed_json[0]['place_name']
    current_date = str(date.today())
    
    amount = '0'
    
    FMT = '%H:%M:%S'
    duration = datetime.strptime(departure_time , FMT) - datetime.strptime(arrival_time , FMT)
    hours = time.strptime(str(duration), FMT)
    x=hours.tm_hour
    if x==1:
        amount = str(30)
    elif x>=2:
        amount=str(int(30)+x*int(10))
    print(v_id,model)
    c.execute("INSERT INTO History VALUES('"+v_id+"','"+model+"','"+arrival_time+"','"+departure_time+"','"+str(slot_no)+"','"+place+"','"+current_date+"','"+amount+"')")
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

