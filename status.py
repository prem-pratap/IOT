#!/usr/bin/env python3
from boltiot import Bolt
import json
API=""#your bolt api
device_id=""#yout bolt device id
mybolt=Bolt(API,device_id)
response=mybolt.isOnline()
print(response)
data=json.loads(response)
print(data["value"])

