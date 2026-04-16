import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dynamic_range = 3.155
pins = [22, 27, 17, 26, 25, 21, 20, 16][::-1]

for i in pins:
    GPIO.setup(i, GPIO.OUT)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за диапазон ЦАП (0,00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    
    return int(voltage / dynamic_range * 255)

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

def number_to_dac(number):
    states = dec2bin(number)
    for i in range(len(pins)):
        GPIO.output(pins[i], states[i])
    print(f"Число на вход ЦАП: {number}, биты: {states}")
    return


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах:"))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
    
finally:
    for i in pins:
        GPIO.output(i, 0)
    GPIO.cleanup()