import adc_plot
import r2r_adc
import time

adc = r2r_adc.R2R_ADC(3.155, 0.0001, False)
voltages = []
times = []
duration = 3

try:
    start = time.time()
    while((time.time() - start) < duration):
        times.append(time.time() - start)
        voltages.append(adc.get_sar_voltage())
    adc_plot.plot_voltage_vs_time(times, voltages, 3.155)
    adc_plot.plot_sampling_period_hist(times)


finally:
    print(len(times))
    adc.deinit()