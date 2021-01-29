from adafruit_motorkit import MotorKit
from time import sleep

pump = MotorKit()

for i in range(5):
    pump.motor1.throttle = 1.0
    sleep(0.82)
    pump.motor1.throttle = 0
    sleep(3)