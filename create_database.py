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


    addHistoryRecord('KA41EN1051','Yelahanka','20:00','21:00','14 Mar 2020','200')
    addHistoryRecord('KA41EN1051','Jayamahal','16:25','18:00','13 Mar 2020','100')
    addHistoryRecord('KA41EN1051','MLA Layout','10:00','13:15','12 Mar 2020','150')
    print('Records added')

    deleteHistoryRecord('KA41EN1051')
    print('Records deleted')
