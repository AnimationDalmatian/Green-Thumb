import time
import board
from adafruit_seesaw.seesaw import Seesaw
import RPi.GPIO as GPIO
import pygame

# intialize speaker sound
file = 'Thirsty2.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

# set the RPi to the Broadcom pin layout
GPIO.setmode(GPIO.BCM)

# uses board.SCL and board.SDA
i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr = 0x36)

# lists to hold measurements from sensor
moistures = []
times = []

def readSensor():
    # read moisture level through capacitive tough pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    
    # get current time
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    
    # add data to lists   
    moistures.append(touch)
    times.append(currentTime)
    
    # play sound
    total = 0
    for num in moistures:
        total += num
    total /= len(moistures)
    if (total <= 800):
        pygame.mixer.music.play()
   
    #print(f"Temp: {temp} \t Moisture: {touch}")
    print(f"Moisture list: {moistures}")
    print(f"Time list: {times}")
    time.sleep(.1)
    
  