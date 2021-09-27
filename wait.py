#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 23
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM) #GPIO.BOARD
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    pressed = False
    while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.BOTH)
        if GPIO.input(BUTTON_GPIO):
            print("Button pressed!")
        else:
            print("released!")
        
