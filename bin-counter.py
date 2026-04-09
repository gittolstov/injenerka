import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


leds = [24, 22, 23, 27, 17, 25, 12, 16]
button = 13

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

state = 0
period = 1.0

while True:
    state += 1
    if state >= 0b100000000:
        state = 0
    time.sleep(period)
    states = dec2bin(state)
    for i in range(8):
        GPIO.output(leds[i], states[i])
        
