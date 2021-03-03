from time import sleep
from gpiozero import Button

Orange = Button(4, pull_up=False)
Red = Button(5, pull_up=False)
Blue = Button(21, pull_up=False)

while True:
    if Orange.is_pressed:
        print("Orange Pressed")
    if Red.is_pressed:
        print("Red Pressed")
    if Blue.is_pressed:
        print("Blue Pressed")
    if Orange.is_pressed and Red.is_pressed:
        print("Orange and Red Pressed")
    if Orange.is_pressed and Blue.is_pressed:
        print("Orange and Blue Pressed")
    if Blue.is_pressed and Red.is_pressed:
        print("Blue and Red Pressed")
    else:
        print("Nothing Pressed")