# new rough skeleton of moisture sensor code with new sensor

import time
import board
from adafruit_seesaw.seesaw import Seesaw
import RPi.GPIO as GPIO

# set the RPi to the Broadcom pin layout
GPIO.setmode(GPIO.BCM)

# uses board.SCL and board.SDA
i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr = 0x36)

'''moistures = {}
temps = {}'''

moistures = []
times = []


while(True):
    # read moisture level through capacitive tough pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    
    # get current time
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    
    # add data to dictionary
    '''moistures[currentTime] = touch
    temps[currentTime] = temp'''
    
    moistures.append(touch)
    times.append(currentTime)
    
    
    
    print(f"Temp: {temp} \t Moisture: {touch}")
    print(f"Moisture list: {moistures}")
    print(f"Time list: {times}")
    #print(f"Temp dict: {temps}")
    time.sleep(3)
    
  