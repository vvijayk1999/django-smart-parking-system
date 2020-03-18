import sqlite3

global conn
conn = sqlite3.connect('smart_parking_system.db')
global c
c = conn.cursor()


def createHistoryTable():
    try:
        c.execute('''CREATE TABLE History
        (v_id text ,place text,arrival_time text,departure_time text,date text,amount text)''')
        print ("table History done")
        conn.commit()
    except:
        print("Table History is already created")

def addHistoryRecord(v_id,place,arrival_time,departure_time,date,amount):
    c.execute("INSERT INTO History VALUES('"+v_id+"','"+place+"','"+arrival_time+"','"+departure_time+"','"+date+"','"+amount+"')")
    conn.commit()

def deleteHistoryRecord(v_id):
    c.execute("DELETE FROM History WHERE v_id='"+v_id+"'")
    conn.commit()

if __name__ == "__main__":
    createHistoryTable()


    addHistoryRecord('ka04781ff','taj hotel','20:00','21:00','14 Mar 2020','200')
    
    print('Records added')

    #deleteHistoryRecord('KA41EN1051')
    print('Records deleted')
