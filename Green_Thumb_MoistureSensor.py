# Just the skeleton of this program; all it does is detect water from a glass.
# After reading a little about this sensor, what is written right now is 
# the simplest for this sensor to just work. 


import RPi.GPIO as GPIO
import time

#GPIO setup
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if (GPIO.input(channel)):
        print("no water detected!")
    else:
        print("water detected!")

# let us knoow when the pin goes HIGH to LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300) 

# assign function to GPIO pin, run function on change
GPIO.add_event_callback(channel, callback)

#infinite loop
while(True):
    time.sleep(1)