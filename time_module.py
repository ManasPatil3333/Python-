# My logic :

import time
obj = time.localtime()
# --> output : time.struct_time(tm_year=2024, tm_mon=5, tm_mday=27, tm_hour=19, tm_min=2, tm_sec=1, tm_wday=0, tm_yday=148, tm_isdst=0)
time1 = time.asctime(obj)
# --> output : Mon May 27 19:03:18 2024
H = obj.tm_hour
M = obj.tm_min
if ( H>=6 and H<12) :
    print(time1, "\nGood Morning...")
elif ( H>12 and H<17) :
    print(time1, "\nGood Afternoon...")
elif ( H>17 and H<20) :
    print(time1, "\nGood Evening...")
else :
    print(time1, "\nGood night...")


# Tutor's logic :
'''
import time 
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp1 = time.strftime("%H")
print(timestamp1)
timestamp2 = time.strftime("%M")
print(timestamp2)
timestamp3 = time.strftime("%S")
print(timestamp3)
'''
