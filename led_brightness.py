#!/usr/bin/env python3
from tkinter import *
from boltiot import Bolt
import json
start=Tk()
start.geometry("300x200+100+100")
start.title("Led ControL along with brightness")
def on():
    response=mybolt.isOnline()
    data=json.loads(response)
    if data["value"]=="online":
        mybolt.digitalWrite('0','HIGH')#0 is the gpio pin
    else:
        print("Your device is offline")
def off():
    response=mybolt.isOnline()
    data=json.loads(response)
    print(data)	
    if data["value"]=="online":
        mybolt.digitalWrite('0','LOW')#0 is the gpio pin
    else:
        print("Your device is offline")#function to change intensity of led
def set_value():
    value=s.get()
    response=mybolt.isOnline()
    if 'online' in response:
        mybolt.analogWrite('0',value)#first arguement is pin number and second is intensity value from 0 to 255
    else:
        print("Your device is offline")    

#Creating a top frame
topframe=Frame(start,width=300,height=150)
lab=Label(topframe,text="Led Control")
lab.pack(fill=X)
Butt1=Button(topframe,text="ON",command=on)
Butt1.pack()
Butt2=Button(topframe,text="OFF",command=off)
Butt2.pack()
topframe.pack()
#creating bottom frame for led brightness control
bottomframe=Frame(start)
label=Label(bottomframe,text="Led Brightness Manager")
label.pack(fill=X)
s=Scale(bottomframe,from_=0,to=255,length=200,width=20,sliderlength=20,orient=HORIZONTAL)
s.pack()
butt3=Button(bottomframe,text="Set Value",command=set_value)
butt3.pack()
bottomframe.pack(side=BOTTOM)

#Bolt led control code
API=""
device_id=""
mybolt=Bolt(API,device_id)
start.mainloop()
