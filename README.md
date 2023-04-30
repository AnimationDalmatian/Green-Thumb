Project Green Thumb
The Fabulous Trio
Zoe Baker, Kaylee Matic, Kelsie Culbret



Description: 
Project Green Thumb is designed to use a moisture sensor and read the amount of moisture the soil in a plant has. Once the moisture level in the soil drops too low, an audio file will be played telling the user that the plant needs to be watered. The user will be able to see a graph of each reading and the time through a GUI. This GUI also contains a chart of all readings, a watering schedule, and settings the user can change for more customization. 

Materials Needed: 
- Adafruit Moisture Sensor
o https://www.adafruit.com/product/4026 
- Wires for Moisture Sensor
o https://www.adafruit.com/product/3955 
- Raspberry Pi with GPIO 
- Any desired plant

Necessary Library Downloads/Setup Procedures 
- Download Adafruit library
o Use command “sudo pip3 install adafruit-circuitpython-seesaw” 
- Download metaplot 
o Use command “pip install matplotlib” 
- On raspberry pi, make sure I2C is enabled
o Go to raspberry pi configurations and under the “interfaces” tab, make sure I2C is enabled
- Connecting sensor to GPIO
o Black wire to Ground
o Red wire to 3V
o White wire to SDA
o Green wire to SCL
- More information about moisture sensor
o https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/overview 


**Open Green_Thumb_GUI.py file to run and test full project**
