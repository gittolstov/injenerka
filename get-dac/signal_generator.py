import time
import numpy

def get_sin_wave_amplitude(freq, time):
    return (1 + numpy.sin(2*numpy.pi*freq*time))/2

def get_trig_wave_amplitude(freq, time):
    return numpy.abs((freq*time + 0.25) - numpy.round(freq*time + 0.25)) * 2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)
