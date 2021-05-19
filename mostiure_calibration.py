import numpy as np #library for performing math in your code
#libraries and code for creating i2c communication
import board
import busio
from time import sleep
i2c = busio.I2C(board.SCL, board.SDA)

#library for communicating with the ADS1115
import adafruit_ads1x15.ads1115 as ADS
#import code for making an analog reading on your ADC
from adafruit_ads1x15.analog_in import AnalogIn
#Create an object from the ADS library
ads = ADS.ADS1115(i2c)

raw_reading0 = AnalogIn(ads, ADS.P0) #take a raw reading from the ADS1115 on channel 0 (first channel)
raw_reading1 = AnalogIn(ads, ADS.P1) #take a raw reading from the ADS1115 on channel 0 (first channel)
raw_reading2 = AnalogIn(ads, ADS.P2) #take a raw reading from the ADS1115 on channel 0 (first channel)
raw_reading3 = AnalogIn(ads, ADS.P3) #take a raw reading from the ADS1115 on channel 0 (first channel)

volumes = [200.0, 175.0, 150.0, 125.0, 100.0, 75.0, 50.0, 25.0, 0.0]
values = [8832.0, 8984.0, 9176.25, 9284.0, 9420.0, 9258.0, 9496.0, 9900.0, 18080.0]
while True:
    calc = np.interp(raw_reading0.value, values, volumes)#interpert the values and have it rint how much water is in
    print(calc)
    print("Sensor 0:", raw_reading0.value)
    print("Sensor 1:", raw_reading1.value)
    print("Sensor 2:", raw_reading2.value)
    print("Sensor 3:", raw_reading3.value)
    sleep(3)