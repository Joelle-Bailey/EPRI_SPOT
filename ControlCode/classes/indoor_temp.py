##############################################################################
#                     Indoor Temperature Class Python Script
# This python script defines the logic necessary to retrieve data from the
# Indoor temperature sensor module from the SHTC3 IC using I2C.
# 
# The operation / main loop this script is tied to is found in
# /ControlCode/operations/climate_main.py
# 
# Template used by flask webserver
# 'indoor_weather': {
#                 'temperature' : None,
#                 'relative_humidity' : None
#             }
#
# Created by Joelle Bailey for EPRI_SPOT, Spring 2024
##############################################################################

from classes.mqtt_connection import MQTT_Connection

import time
import board
import adafruit_shtc3
import json

class Indoor_Temp():
    def __init__(self, mqtt_connect = MQTT_Connection(type='publisher')):
        self.i2c = board.I2C()   # uses board.SCL and board.SDA
        self.sht = adafruit_shtc3.SHTC3(self.i2c)
        self.mqtt_client = mqtt_connect
    
    def get_reading(self):
        temperature, relative_humidity = self.sht.measurements
        return temperature, relative_humidity
    
    def publish_reading(self):
        temp, humid = self.get_reading()
        data = {'temperature': temp, 'relative_humidity': humid}
        
        self.mqtt_client.publishAsJSON('indoor_weather', data)
        print(f"Published to \'indoor_weather\':\n{data}")
