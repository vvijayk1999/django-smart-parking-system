from datetime import datetime

FMT = '%H:%M:%S'

departure_time = '00:12:00' 
arrival_time = '00:12:00'
duration = datetime.strptime(departure_time , FMT) - datetime.strptime(arrival_time , FMT)
amount='30'
for duration in range(2,5):
    amount=str(int(amount)+30)
print('arrival time : '+ arrival_time)
print('departure time : '+ departure_time)
print(amount)