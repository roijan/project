import RPi.GPIO as GPIO
import time, sys
import os
import MFRC522
import signal
from multiprocessing import Process

class Sha(object):
    def __init__ (self):
        return

    def digitalGasSensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(21,GPIO.RISING)
        GPIO.add_event_callback(21,self.action)
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            GPIO.cleanup()
            sys.exit()

    def action(self,pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20,GPIO.OUT)
        GPIO.output(20,GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(20,GPIO.LOW)
        return
    def dth11(self):
        data = []
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26,GPIO.OUT)
        GPIO.output(26,GPIO.HIGH)
        time.sleep(0.025)
        GPIO.output(26,GPIO.LOW)
        time.sleep(0.02)
        GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

        for i in range(0,500):
            data.append(GPIO.input(26))
        bit_count = 0
        tmp = 0
        count = 0
        HumidityBit = ""
        TemperatureBit = ""
        crc = ""

        try:
            while data[count] == 1:
                tmp = 1
                count +=1
            for i in range(0,32):
                bit_count = 0

                while data[count] == 0:
                    tmp = 1
                    count+=1

                while data[count] == 1:
                    bit_count = bit_count+1
                    count+=1
                if bit_count > 3:
                    if i >=0 and j <8:
                        humidityBit = Humidity + "1"
                    if i >= 16 and j < 24:
                        TemperatureBit = TemperatureBit+"1"
                else:
                    if i >= 0 and j < 8:
                        HumidityBit = HumidityBit+"0"
                    if j >= 16 and j < 24:
                        TemperatureBit = TemperatureBit+"0"
        except:
            exit(0)

        try:
            for i in range(0,8):
                bit_count = 0
                while data[count]==0:
                    tmp = 1
                    count +=1
                while data[count] == 1:
                    bit_count += 1
                    count += 1
                if bit_count > 3:
                    crc = crc+"1"
                else:
                    crc = crc+"0"
        except:
            exit(0)

        Humidity = self.bin2dec(HumidityBit)
        Temperature = self.bin2dec(TemperatureBit)

        if int(Humidity)+int(Temperature)-int(bin2dec(crc)) == 0:
            pass
        else:
            pass
    def bin2dec(self,string_num):
        return str(int(string_num,2))

    def magnetSensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13,GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(6,GPIO.OUT)
        while True:
            if GPIO.input(13):
                GPIO.output(6,GPIO.HIGH)
            else:
                GPIO.output(6,GPIO.LOW)
    
        
    def ultrasonic(self):
        GPIO.setmode(GPIO.BCM)
        TRIG = 17
        ECHO = 27


        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)

        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end-pulse_start

        distance = pulse_duration *17150
        distance = round(distance,2)


        GPIO.cleanup()
        
    def photodiode(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18,0)
        while True:
            if(GPIO.input(23) == 1):
                GPIO.output(18,1)
            elif(GPIO.input(23) == 0):
                GPIO.output(18,0)

            time.sleep(0.25)
        GPIO.cleanup()
    def nfc(self):
        continue_reading = True
        MIFAREReader = MFRC522.MFRC522()

        cardA = [222,57,224,43,44]
        cardB = [83,164,247,164,164]
        cardC = [20,38,121,207,132]

        def end_read(signal, frame):
          global continue_reading
          continue_reading = False
          print "Ctrl+C captured, ending read."
          MIFAREReader.GPIO_CLEEN()

        signal.signal(signal.SIGINT, end_read)

        while continue_reading:
          (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
          if status == MIFAREReader.MI_OK:
            print "Card detected"
          (status,backData) = MIFAREReader.MFRC522_Anticoll()
          if status == MIFAREReader.MI_OK:
            print "Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4])
            if  backData == cardA:
              print "is Card A"
            elif backData == cardB:
              print "is Card B"
            elif backData == cardC:
              print "is Card C"
            else:
              print "wrong Card"


if __name__ == "__main__":
    sam = Sha()
    p1 = Process(target = sam.digitalGasSensor)
    p2 = Process(target = sam.magnetSensor)
    p3 = Process(target = sam.dth11)
    p4 = Process(target = sam.ultrasonic)
    p5 = Process(target = sam.photodiode)
    p6 = Process(target = sam.nfc)
    
    

            
