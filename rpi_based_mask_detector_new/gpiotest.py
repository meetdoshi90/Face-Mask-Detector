import RPi.GPIO as GPIO
import time
from time import sleep
import wiringpi as wiringpi

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(15 , 1)
GPIO.output(13 , 1)
GPIO.output(11 , 1)
wiringpi.wiringPiSetup()
wiringpi.pinMode(26, 2)
#wiringpi.softServoSetup()
wiringpi.softPwmCreate(26,0,25)
dutycycle = 0
for dutycycle in range(0,26,1):
    #wiringpi.pwmWrite(26,dutycycle)
    wiringpi.softPwmWrite(26,dutycycle)
    time.sleep(2)
    print(dutycycle)

for dutycycle in range(26,-1,-1):
    #wiringpi.pwmWrite(26,dutycycle)
    wiringpi.softPwmWrite(26,dutycycle)
    time.sleep(2)
    print(dutycycle)
print("GGWP")
""""""
#time.sleep(100)

GPIO.output(15 , 0)
GPIO.output(13 , 0)
GPIO.output(11 , 0)
GPIO.cleanup()
