import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN, GPIO.PUD_UP)
while True:
    if GPIO.input(5):
        print "Switch is open"
    else:
        print "Switch is closed"
        
