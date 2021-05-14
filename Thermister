import numpy as np #library for performing math in your code
#libraries and code for creating i2c communication
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

#library for communicating with the ADS1115
import adafruit_ads1x15.ads1115 as ADS
#import code for making an analog reading on your ADC
from adafruit_ads1x15.analog_in import AnalogIn
#Create an object from the ADS library
ads = ADS.ADS1115(i2c)

#Variables to hold constants
fixed_r = 10000.0 #fixed resistance of resistor in voltage divider (measure in Ohms)
beta_coefficient = 3950.0 #manufaturer information for our specific thermistor
room_temp = 298.15 #What all of the math we will be using is based off of (measured in Kelvins and = 25 deg C)

raw_reading = AnalogIn(ads, ADS.P0) #take a raw reading from the ADS1115 on channel 0 (first channel)

resistance = round(fixed_r/((3.3/raw_reading.voltage)-1.0),1)#convert the voltage reading into the correlated resistance of the thermistor at the time of reading
#print for debugging
print(raw_reading.voltage)
print(resistance)

#Steinhart-Hart Equation used to convert the resistance into the ambient room temperature (measured in Kelvins)
temp_k = np.log(resistance/fixed_r)#Use numpy to find the log of the ratio between our calculated resistance and our fixed resistor
temp_k /= beta_coefficient#now divide by our beta coefficient from the manufacturer
temp_k += (1/room_temp)#add the inverse of the room temperature
temp_k = 1/temp_k#get the inverse of the current value
temp_c = round(temp_k - 273.15, 1)#convert from Kelvins to Celsius

temp_f = temp_c*(9/5)+ 32.0#Convert from Celsius to Fahrenheit
print('temperature: ', temp_c, "C")#print temp in C
print(temp_f, "F")#print temp in F
