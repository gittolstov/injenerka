import RPi.GPIO as GPIO
import time
from math import log10, pow

GPIO.setmode(GPIO.BCM)

led = 26
button = 13
photo = 6

state = 1
duty = 0.0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo, GPIO.IN)

pwm = GPIO.PWM(led, 200)
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)#pow(10, duty / 50)
    time.sleep(0.05)

    duty += 1
    if duty >= 100:
        duty = 0