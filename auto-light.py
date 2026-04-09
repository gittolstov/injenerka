import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
button = 13
photo = 6

state = 1
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo, GPIO.IN)


while True:
    GPIO.output(led, GPIO.input(photo))
    time.sleep(0.2)