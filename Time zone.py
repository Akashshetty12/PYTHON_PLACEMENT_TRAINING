from datetime import datetime
import pytz
'''tz = pytz.timezone("Asia/Kolkata")
b = datetime.now(tz)
b = datetime.time(b)
print(b)'''

s = datetime.strptime("1:00","%H:%M").time()
e = datetime.strptime("2:00","%H:%M").time()
now = datetime.now(pytz.timezone("Asia/Calcutta")).time()
c = now.replace(second=0,microsecond=0)
if s<= c <= e:
    print("Time is within range")
else:
    print("Time is out of range")

#for i in pytz.all_timezones:
    #print(i)