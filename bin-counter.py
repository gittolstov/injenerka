import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


leds = [24, 22, 23, 27, 17, 25, 12, 16][::-1]
button1 = 9
button2 = 10

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

state = 0
period = 1.0

while True:
    inputs = [GPIO.input(button1), GPIO.input(button2)]
    if (not (inputs[0] or inputs[1])):
        continue
    elif inputs[0]:
        state += 1
    elif inputs[1]:
        state -= 1
    if (inputs[0] and inputs[1]):
        state = 0b11111111
    if state >= 0b100000000 or state < 0:
        state = 0
    states = dec2bin(state)
    for i in range(8):
        GPIO.output(leds[i], states[i])
    time.sleep(0.3)
        
        
