from adafruit_motorkit import MotorKit
from time import sleep
from atlas_i2c import atlas_i2c
from Adafruit_IO import Client, Feed

pump = MotorKit()
sensor_address = 2
pH_sensor = atlas_i2c.AtlasI2C()
pH_sensor.set_i2c_address(sensor_address)

while True:
    reading = pH_sensor.query("R", processing_delay=1500)

    pH = reading.data

    pH = round(float(pH.decode("utf-8")),1)
    print(pH)
    if pH > 7.0:
        
        pump.motor1.throttle = 1.0
        sleep(0.82)
        pump.motor1.throttle = 0
        sleep(3)
    

