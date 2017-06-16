#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26,0)
while True:
    if(GPIO.input(16) == 1):
        print("ON")
    elif(GPIO.input(16) == 0):
        print("OFF")

    time.sleep(0.25)
    os.system('clear')
    
    
