# new rough skeleton of moisture sensor code with new sensor

import time
import board
from adafruit_seesaw.seesaw import Seesaw


# uses board.SCL and board.SDA
i2c_bus = board.I2C()

ss = Seesaw(i2c_bus, addr = 0x36)

while(True):
    # read moisture level through capacitive tough pad
    touch = ss.moisture_read()
    
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    
    print("Temp: " + str(temp) + "\t Moisture: " + str(touch))
    time.sleep(1)