import numpy as np #library for performing math in your code
#libraries and code for creating i2c communication
import board
import busio
from time import sleep
from gpio import LED
i2c = busio.I2C(board.SCL, board.SDA)

#library for communicating with the ADS1115
import adafruit_ads1x15.ads1115 as ADS
#import code for making an analog reading on your ADC
from adafruit_ads1x15.analog_in import AnalogIn
#Create an object from the ADS library
ads = ADS.ADS1115(i2c)

relay = LED(17)
num_reading = 20
volumes = [200.0, 175.0, 150.0, 125.0, 100.0, 75.0, 50.0, 25.0, 0.0]
values = [8832.0, 8984.0, 9176.25, 9284.0, 9420.0, 9258.0, 9496.0, 9900.0, 18080.0]

 
while True:
    total0 = 0
    total1 = 0
    total2 = 0
    total3 = 0
    
    for i in range(num_reading):
        raw_reading0 = AnalogIn(ads, ADS.P0)
        raw_reading1 = AnalogIn(ads, ADS.P1)
        raw_reading2 = AnalogIn(ads, ADS.P2)
        raw_reading3 = AnalogIn(ads, ADS.P3)
        total0+= raw_reading0.value
        total1+= raw_reading1.value
        total2+= raw_reading2.value
        total3+= raw_reading3.value
    
    total0/= num_reading
    total1/= num_reading
    total2/= num_reading
    total3/= num_reading

    total_average = (total0 + total1 + total2 + total3) / 4.0
    calct = np.interp(total_average, values, volumes)
    calc0 = np.interp(total0, values, volumes)#interpert the values and have it rint how much water is in
    calc1 = np.interp(total1, values, volumes)
    calc2 = np.interp(total2, values, volumes)
    calc3 = np.interp(total3, values, volumes)
    print("Total Average Moisture:", calct)
    print("Sensor 0 Moisture:", calc0)
    print("Sensor 1 Moisture:", calc1)
    print("Sensor 2 Moisture:", calc2)
    print("Sensor 3 Moisture:", calc3)
    print("RR Sensor 0:", raw_reading0.value)
    print("RR Sensor 1:", raw_reading1.value)
    print("RR Sensor 2:", raw_reading2.value)
    print("RR Sensor 3:", raw_reading3.value)
    
    if calct < 20:
        relay.on()
        sleep (57)
        relay.off()
    sleep(60)
    
