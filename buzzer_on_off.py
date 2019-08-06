#!/usr/bin/env python3
from tkinter import *
from boltiot import Bolt
start=Tk()
start.geometry("300x300+100+100")
start.title("Buzzer On Off")
def on():
    mybolt.digitalWrite('0','HIGH')
    print(mybolt.isOnline())
    print("High")
def off():
    mybolt.digitalWrite('0','LOW')
    print(mybolt.isOnline())
    print("Low")
Butt1=Button(start,text="ON",command=on)
Butt1.pack()
Butt2=Button(start,text="OFF",command=off)
Butt2.pack()
#Bolt buzzer control code
API="977c628f-04b5-4b57-a3a9-ccbc58708fbf"
device_id="BOLT1116997"
mybolt=Bolt(API,device_id)
start.mainloop()
#9413266522
