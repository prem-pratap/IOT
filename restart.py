#!/usr/bin/env python3
from boltiot import Bolt
API=""#yur bolt device  api
device_id=""#your bolt device id
mybolt=Bolt(API,device_id)
print(mybolt.restart())
