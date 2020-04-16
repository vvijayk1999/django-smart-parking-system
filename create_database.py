import sqlite3

global conn
conn = sqlite3.connect('smart_parking_system.db')
global c
c = conn.cursor()


def createHistoryTable():
    try:
        c.execute('''CREATE TABLE History
        (v_id text ,place text,arrival_time text,departure_time text,date text,amount text)''')
        print ("table History created")
        conn.commit()
    except:
        print("Table History is already created")

def createSlotsTable():
    try:
        c.execute('''CREATE TABLE Slots
        (slot_num text,status text,place text)''')
        print ("table Slots created")
        conn.commit()
    except:
        print("Table Slots is already created")

def createRealtimeSlotsTable():
    try:
        c.execute('''CREATE TABLE RealtimeSlots
        (slot_num text,status text,place text)''')
        print ("table RealtimeSlots created")
        conn.commit()
    except:
        print("Table RealtimeSlots is already created")

def createOnline_slotsTable():
    try:
        c.execute('''CREATE TABLE Online_slots
         (slot_num int,status text,place text,current_date text,PRIMARY KEY(slot_num,place))''')
        conn.commit()
    except:
        print("Table RealtimeSlots is already created")

def addHistoryRecord(v_id,place,arrival_time,departure_time,date,amount):
    c.execute("INSERT INTO History VALUES('"+v_id+"','"+place+"','"+arrival_time+"','"+departure_time+"','"+date+"','"+amount+"')")
    conn.commit()

def deleteHistoryRecord(v_id):
    c.execute("DELETE FROM History WHERE v_id='"+v_id+"'")
    conn.commit()

def deleteAllSlotRecord():
    c.execute("DELETE FROM Slots")
    conn.commit()

def addRealtimeSlotsRecord(slot_num,status,place):
    c.execute("INSERT INTO RealtimeSlots VALUES('"+slot_num+"','"+status+"','"+place+"')")
    conn.commit()

def addOnline_slots(slot_num,status,place,current_date):
    c.execute("INSERT INTO Online_slots VALUES('"+slot_num+"','"+status+"','"+place+"','"+current_date+"')")
    conn.commit()

def deleteAllRealtimeRecords():
    c.execute('DELETE FROM RealtimeSlots')
    conn.commit()

if __name__ == "__main__":
    #createHistoryTable()
    #createSlotsTable()

    #addHistoryRecord('ka04781ff','taj hotel','20:00','21:00','14 Mar 2020','200')
    #deleteAllSlotRecord()
    #print('Records added')

    # createRealtimeSlotsTable()
    # addRealtimeSlotsRecord('1','0','mantri-mall')
    # addRealtimeSlotsRecord('2','1','mantri-mall')
    # addRealtimeSlotsRecord('3','0','mantri-mall')
    # addRealtimeSlotsRecord('4','2','mantri-mall')

    addOnline_slots('1','0','mantri-mall','sdlkfsd')
    addOnline_slots('2','2','mantri-mall','sdlkfsd')
    addOnline_slots('3','0','mantri-mall','sdlkfsd')
    # createOnline_slotsTable()

    #c.execute("DELETE FROM Online_slots")
    # c.execute("DROP TABLE Online_slots")
    # conn.commit()

    # deleteAllRealtimeRecords()

    #deleteHistoryRecord('KA41EN1051')
    #print('Records deleted')
