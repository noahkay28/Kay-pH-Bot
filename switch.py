from time import sleep
from gpiozero import Button

red = Button(16, pull_up=False)
blue = Button(20, pull_up=False)
orange = Button(21, pull_up=False)

while True:
    if red.is_pressed:
        print("red")
    if blue.is_pressed:
        print("blue")
    if orange.is_pressed:
        print("orange")
     if orange.is_pressed and red.is_pressed:
        print("Orange and Red Pressed")
    if orange.is_pressed and blue.is_pressed:
        print("Orange and Blue Pressed")
    if blue.is_pressed and red.is_pressed:
        print("Blue and Red Pressed")
    else:
        print("Nothing Pressed")
