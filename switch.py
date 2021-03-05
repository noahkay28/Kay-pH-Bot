from time import sleep
from gpiozero import Button

red = Button(16, pull_up=False)
blue = Button(20, pull_up=False)
orange = Button(21, pull_up=False)

while True:
    if red.is_pressed:
        if blue.value == 0 and orange.value == 0:
            print("red")
    if blue.is_pressed:
        if red.value == 0 and orange.value == 0:
            print("blue")
    if orange.is_pressed:
        if red.value == 0 and blue.value == 0:
            print("orange")
    if orange.is_pressed and red.is_pressed:
        if blue.value == 0:
            print("Orange and Red Pressed")
    if orange.is_pressed and blue.is_pressed:
        if red.value == 0:
            print("orange and blue")
    if blue.is_pressed and red.is_pressed:
        if orange.value == 0:
            print("blue and red")
    if blue.is_pressed and red.is_pressed and orange.is_pressed:
        print("everything")
    if blue.value == 0 and red.value == 0 and orange.value == 0:
        print("Nothing Pressed")
sleep(1)
