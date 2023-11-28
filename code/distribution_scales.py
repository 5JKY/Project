from data_generate import selling_rates

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

mpl.rcParams.update({
    'figure.figsize': [15, 8]
})

# Plot standard deviation for each year, quarter, and month, find Volatility Over Time
selling_rates.resample('M').std().plot(style=':', label='Monthly', marker='^')
selling_rates.resample('BQS').std().plot(style='--', label='Quarterly', marker='x')
selling_rates.resample('BAS').std().plot(style='-', label='Yearly', marker='o')

plt.title('Standard Deviations at Different Time Scales')
plt.xlabel('date')
plt.ylabel('Standard Deviation (CNY/100CAD)')
plt.legend()
plt.savefig('graphs/std_scales.pdf')
plt.show()


# Resample data to observe trend and variability in quarterly scale
mean_quarterly = selling_rates.resample('BQS').mean()
max_quarterly = selling_rates.resample('BQS').max()
min_quarterly = selling_rates.resample('BQS').min()


# Plot every forex trading day with reduced alpha for better visibility
selling_rates.plot(alpha=0.3, style='-', label='Every Forex Trading Day')

# Plot mean, max, and min values for each quarter with different markers
mean_quarterly.plot(style=':', label='Mean Value of Each Quarter', marker="o")
max_quarterly.plot(style='r:', label='Maximum Value of Each Quarter', marker="^")
min_quarterly.plot(style='g:', label='Minimum Value of Each Quarter', marker="v")

# Customize the plot
plt.title('Quarterly Mean and Extreme Value Trend')
plt.xlabel('Date')
plt.ylabel('Exchange Rate (CNY/100CAD)')
plt.legend()
plt.savefig('graphs/distribution_quaterly.pdf')
plt.show()


# Resample data to observe trend and variability in monthly scale
max_monthly = selling_rates.resample('BMS').max()
min_monthly = selling_rates.resample('BMS').min()
mean_monthly = selling_rates.resample('BMS').mean()


# Plot maximum, minimum, and mean values for each month with different markers
mean_monthly.plot(style=':', label='Mean Value of Each Month', marker='o', markersize=5)
max_monthly.plot(style='r:', label='Maximum Value of Each Month', marker='^', markersize=5)
min_monthly.plot(style='g:', label='Minimum Value of Each Month', marker='v', markersize=5)

# Customize the plot
plt.title('Monthly Mean and Extreme Value Trend')
plt.xlabel('Date')
plt.ylabel('Exchange Rate (CNY/100CAD)')
plt.legend()
plt.savefig('graphs/distribution_monthly.pdf')
plt.show()
