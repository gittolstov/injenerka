import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        print(gpio_bits)
        GPIO.setup(gpio_bits, GPIO.OUT)
        return
    
    def set_voltage(self, voltage):
        self.number_to_dac(self.voltage_to_number(voltage))
        return
    
    def dec2bin(self, val):
        return [int(element) for element in bin(val)[2:].zfill(8)]
    
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за диапазон ЦАП (0,00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / self.dynamic_range * 255)
    
    def number_to_dac(self, number):
        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {self.dec2bin(number)}")
        GPIO.output(self.gpio_bits, self.dec2bin(number))
        return
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        return


if __name__ == "__main__":
    try:
        dynamic_range = 3.155
        pins = [22, 27, 17, 26, 25, 21, 20, 16][::-1]
        dac = R2R_DAC(pins, dynamic_range)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
        
    finally:
        dac.deinit()