import board
import adafruit_mlx90614
from time import sleep
i2c = board.I2C()

sensor1 = adafruit_mlx90614.MLX90614(i2c, address=0x5A)#creating sensor objects
sensor2 = adafruit_mlx90614.MLX90614(i2c, address=0x5B)
sensor3 = adafruit_mlx90614.MLX90614(i2c, address=0x5C)
num_readings = 3
dewpoint = 20#we get this form berin


while True:
    temp1 = round(((sensor1.object_temperature*9/5)+32),1) #take readings and convert from celcius to fairenheit
    temp2 = round(((sensor2.object_temperature*9/5)+32),1)
    temp3 = round(((sensor3.object_temperature*9/5)+32),1)
    
    avg_temp = round((temp1 + temp2 + temp3)/num_readings,1)
    Rhumidity= 5*(dewpoint - avg_temp)+100
    VPSat = (610.7*10**((7.5*avg_temp)/(237.3+avg_temp)))/1000
    VPair = VPSat*Rhumidity/1000
    VPD = VPSat - VPair
    
    print("Relative Humidity:", Rhumidity)
    print("VPD:", VPD)
    print("Average Temp: ", avg_temp)
    print('sensor 1 temp: ', temp1)
    print('sensor 2 temp: ',temp2)
    print('sensor 3 temp: ',temp3)    
    
    sleep(1)



