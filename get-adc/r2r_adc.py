import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
        return
    

    def number_to_dac(self, number):
        if (number < 0 or number > 255 or int(number) != number):
            print(f"Error: number is {number}")
            return
        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {self.dec2bin(number)}")
        GPIO.output(self.bits_gpio, self.dec2bin(number))
        return

    
    def dec2bin(self, val):
        return [int(element) for element in bin(val)[2:].zfill(8)]


    def sequential_counting_adc(self):
        counter = 0
        while (True):
            self.number_to_dac(counter)
            time.sleep(self.compare_time)
            if (counter >= 255 or GPIO.input(self.comp_gpio) != 0):
                break
            counter += 1
        return counter - 1

    
    def successive_approximation_adc(self):
        weight = 128
        counter = 0
        while weight >= 1:
            self.number_to_dac(counter + weight)
            time.sleep(self.compare_time)
            if (GPIO.input(self.comp_gpio) == 0):
                counter += weight
            weight //= 2
        return counter - 1


    def get_sc_voltage(self):
        return self.sequential_counting_adc() / 255 * self.dynamic_range

    
    def get_sar_voltage(self):
        return self.successive_approximation_adc() / 255 * self.dynamic_range


    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        return


if __name__ == "__main__":
    try:
        dynamic_range = 3.155
        adc = R2R_ADC(dynamic_range)
        while True:
            try:
                print(adc.get_sc_voltage())
            except ValueError:
                print("ОШЫПКА\n")
        
    finally:
        adc.deinit()