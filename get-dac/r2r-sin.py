import signal_generator as sg
import r2r_dac as r2r
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
start = time.time()

if __name__ == "__main__":
    try:
        dynamic_range = 3.155
        pins = [22, 27, 17, 26, 25, 21, 20, 16][::-1]
        dac = r2r.R2R_DAC(pins, dynamic_range)
        while True:
            dac.set_voltage(sg.get_trig_wave_amplitude(signal_frequency, time.time() - start))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()