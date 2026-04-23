import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.verbose = verbose
        self.dynamic_range = dynamic_range

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(gpio_pin, pwm_frequency)
        self.pwm.start(0)
        return
    
    def set_voltage(self, voltage):
        self.number_to_dac(self.voltage_to_number(voltage))
        return
    
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за диапазон (0,00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / self.dynamic_range * 100)
    
    def number_to_dac(self, number):
        if self.verbose:
            print(f"Активность ШИМ: {number}%")
        
        self.pwm.ChangeDutyCycle(number)
        return
    
    def deinit(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.cleanup()
        return


if __name__ == "__main__":
    try:
        
        dac = PWM_DAC(12, 500, 3.183, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах:"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
        
    finally:
        dac.deinit()