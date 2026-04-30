from matplotlib import pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10, 6))
    plt.plot(time, voltage)
    plt.show()
    return

def plot_sampling_period_hist(times):
    sampling_periods = [times[i+1] - times[i] for i in range(len(times) - 1)]
    plt.figure(figsize = (10, 6))
    plt.hist(sampling_periods)
    plt.xlim(0, 0.06)
    plt.show()
    return


if __name__ == "__main__":
    plot_voltage_vs_time([1, 2, 3], [1.0, 1.3, 1.2], 3)