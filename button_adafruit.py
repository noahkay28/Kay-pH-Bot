#motor wont turn off on auto
from time import sleep
from Adafruit_IO import Client, Feed
from adafruit_motorkit import MotorKit
from atlas_i2c import atlas_i2c

io_key = "94921b4b90264ebbb2b0fc9a08137e9e"
io_username = "reginius214"
sensor_address = 2
pH_sensor = atlas_i2c.AtlasI2C()
pH_sensor.set_i2c_address(sensor_address)

aio = Client(io_username, io_key)
pump_button = aio.feeds('kay-pump')
toggle = aio.feeds('kay-toggle')
slider = aio.feeds('kay-dosage')
pH_High_Point = aio.feeds ('kay-ph-high')
pH_Low_Point = aio.feeds ('kay-ph-low')
pump = MotorKit()

while True:
    reading = pH_sensor.query("R", processing_delay = 1500)
    pH = reading.data
    pH = round(float(pH.decode("utf-8")),1)
    toggle_value = aio.receive(toggle.key)
    mode = toggle_value.value
    if mode == "Manual":
        button_value = aio.receive(pump_button.key)
        result = button_value.value
        if result == "1":
            slider_value = aio.receive(slider.key)
            volume = slider_value.value
            pump.motor1.throttle = 1.0
            sleep(int(volume))
            pump.motor1.throttle = 0
    elif mode == "Auto":
        low_point = aio.receive(pH_Low_Point.key)
        low_point_value = low_point.value 
        if pH < float(low_point_value):
            pump.motor1.throttle = 1.0
            sleep(int(volume))
            pump.motor1.throttle = 0
 sleep(0.5)
    
    
