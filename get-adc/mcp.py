import adc_plot
import mcp3021_driver
import time

adc = mcp3021_driver.MCP3021(3.155, False)
voltages = []
times = []
duration = 20

try:
    start = time.time()
    while((time.time() - start) < duration):
        times.append(time.time() - start)
        voltages.append(adc.get_voltage())
    adc_plot.plot_voltage_vs_time(times, voltages, 3.155)
    adc_plot.plot_sampling_period_hist(times)



finally:
    print(len(times))
    adc.deinit()