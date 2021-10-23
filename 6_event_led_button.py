#!/usr/bin/env python3          
                                
import signal                   
import sys
import RPi.GPIO as GPIO
BUTTON_GPIO = 17
LED_GPIO = 20
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_callback(channel):
    if GPIO.input(BUTTON_GPIO):
        print("Button pressed!")
        GPIO.output(LED_GPIO, GPIO.HIGH)
    else:
        print("Button released!")
        GPIO.output(LED_GPIO, GPIO.LOW)
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_GPIO, GPIO.OUT)   

    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
            callback=button_callback, bouncetime=50)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    
