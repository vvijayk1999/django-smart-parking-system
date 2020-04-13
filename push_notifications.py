from pyfcm import FCMNotification
import sqlite3

global conn
conn = sqlite3.connect('smart_parking_system.db')
global c
c = conn.cursor()

push_service = FCMNotification(api_key="AAAAj7P1O5g:APA91bHUCdu3Pf3pdewj2co-rQO9yFwkWjTm2FKbvHNrMZwrWw6KZ2OUDy_sdilVTXTdBg7KqWh6EH3rt6P34CXNpYrdgSC3eJMPjY-iwx_a5rXXmPCCCUITurpYLpl-Kfe2rz2oNHBn")

def sendPushNotifications(v_id,message_string):

    try:
        c.execute("SELECT email FROM users_vid WHERE v_id = '%s'" %v_id)
        result=c.fetchall()
        for row in result:

            topic = row[0].split('@')[0]+'%'+row[0].split('@')[1]
            
            print(topic)

            message_title = "Smart Parking System"
            result = push_service.notify_topic_subscribers(topic_name=topic, message_body=message_string,message_title=message_title)
    except:
        pass

v_id = 'dfwe885'
message_string = 'nigga you parked'

if __name__ == "__main__":
    sendPushNotifications(v_id,message_string)
