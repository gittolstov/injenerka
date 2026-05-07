import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
        self.num_range = 1024
        return
    
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number

    def get_voltage(self):
        return self.get_number() / self.num_range * self.dynamic_range
    
    def dec2bin(self, val):
        return [int(element) for element in bin(val)[2:].zfill(8)]

    def deinit(self):
        self.bus.close()
        return


if __name__ == "__main__":
    try:
        dynamic_range = 5.17
        adc = MCP3021(dynamic_range, True)
        while True:
            try:
                print(adc.get_voltage())
                time.sleep(1)
            except ValueError:
                print("ОШЫПКА\n")
        
    finally:
        adc.deinit()