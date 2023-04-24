# new rough skeleton of moisture sensor code with new sensor

import time
import board
from adafruit_seesaw.seesaw import Seesaw


moistures = {}
temps = {}

# uses board.SCL and board.SDA
i2c_bus = board.I2C()

ss = Seesaw(i2c_bus, addr = 0x36)

while(True):
    # read moisture level through capacitive tough pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    
    # get current time
    t = time.localtime()
    currentTime = time.strftime("%H:%M:S", t)
    
    # add data to dictionary
    moistures[currentTime] = touch
    temps[currentTime] = temp
    
    
    print(f"Temp: {temp} \t Moisture: {touch}")
    print(f"Moisture dict: {moistures}")
    print(f"Temp dict: {temps}")
    time.sleep(1)
    
    
    
    
    
"""    
SDA_PIN = 23
SCL_PIN = 22

i2c = machine.I2C(sda = machine.Pin(SDA_PIN), scl = machine.Pin(SCL_PIN), freq = 400000)
seesaw = StemmaSoilSensor(i2c)

while(True):
    # get temp and moisture
    moisture = seesaw.get_moisture()
    temp = seesaw.get_temp()
    
    #get current time
    t = time.localtime()
    currentTime = time.strftime("%H:%M:S", t)
    
    # add data to dictionary
    moistures[currentTime] = moisture
    temps[currentTime] = temp
    
    
    print(f"Temp: {temp} \t Moisture: {moisture}")
    print(f"Moisture dict: {moistures}")
    print(f"Temp dict: {temps}")
    time.sleep(1)
"""