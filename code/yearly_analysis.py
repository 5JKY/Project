from data_generate import selling_rates

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

mpl.rcParams.update({
    'figure.figsize': [15, 8]
})

selling_rates.resample('BA').mean().plot(style=':', label='mean value of each year', marker='o', markersize=5)
selling_rates.resample('BA').median().plot(style=':', label='median value of each year', marker='o', markersize=5)
# selling_rates.asfreq('BAS').plot(style='--', label='sample the start of each year', marker='^')
selling_rates.resample('BA').max().plot(style=':', label='maximum value of each year', marker='x')
selling_rates.resample('BA').min().plot(style=':', label='minumum value of each year', marker='x')

# Set title and labels 
plt.title('Yearly Analysis of Forex Trading Rates')
plt.xlabel('Year')
plt.ylabel('Exchange Rate')
# Show and save figure
plt.legend()
plt.savefig('graphs/yearly_analysis.pdf')
plt.show()


# Calculate the mean value per year
mean_per_year = selling_rates.resample('AS').mean()
# Define five distinct colors for each year
colors = ['blue', 'green', 'orange', 'purple', 'red']

# Plot the original data and the mean values
plt.plot(selling_rates, label='Original Data')
for (date, mean_value), color in zip(mean_per_year.items(), colors):
    year_start = pd.Timestamp(f'{date.year}-01-01')
    year_end = pd.Timestamp(f'{date.year+1}-01-01')
    plt.hlines(mean_value, year_start, year_end, linestyle='--', colors=color, label=f'Mean Value {date.year}')

# Set title and labels
plt.title('Daily Exchange Rates with Mean Value per Year')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
# Show and save figure
plt.legend()
plt.savefig('graphs/daily_rates_with_yearly_mean.pdf')
plt.show()
