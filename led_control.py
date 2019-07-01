#!/usr/bin/env python3
from tkinter import *
from boltiot import Bolt
start=Tk()
start.geometry("300x300+100+100")
start.title("Led ControL")
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
#Bolt led control code
API=""
device_id=""
mybolt=Bolt(API,device_id)
start.mainloop()
