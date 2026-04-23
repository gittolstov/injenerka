import signal_generator as sg
import mcp4725_driver as mcp
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
start = time.time()

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(5.18, 0x61, False)
        while True:
            dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, time.time() - start))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()