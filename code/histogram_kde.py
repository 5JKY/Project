from data_generate import selling_rates

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

mpl.rcParams.update({
    'figure.figsize': [15, 8]
})

# Display a histogram for a more detailed view of the data distribution in about 5 years range
seaborn.histplot(selling_rates, bins=70, kde=True)
plt.title('Histogram with KDE for overall time series')
plt.xlabel('Exchange Rates')
plt.ylabel('Frequency')
plt.savefig('graphs/overall_hist.pdf')
plt.show()


# Plot histogram for each year, from 2019 to 2022
start_date = '2019-01-01'
end_date = '2022-12-31'

# Divide the time series into four yearly intervals and plot histograms with KDE for each year
years = range(int(start_date[:4]), int(end_date[:4])+1, 1)

fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

for i, year in enumerate(years):
    start_interval = f'{year}-01-01'
    end_interval = f'{year}-12-31'
    interval_data = selling_rates[start_interval:end_interval]

    ax = axes[i // 2, i % 2]
    seaborn.histplot(interval_data, kde=True, bins=70, ax=ax)
    ax.set_title(f'Histogram and KDE for {year}')
    ax.set_xlabel('Exchange Rates')
    ax.set_ylabel('Frequency')
  
plt.tight_layout()
plt.savefig('graphs/subplot_yearly_hist.pdf')
plt.show()


# Display a histogram for 2023, which only records exchange rates data before 2023-11-01
seaborn.histplot(selling_rates['2023-01-01':'2023-11-1'], bins=70, kde=True)
plt.title('Histogram with KDE for 2023 before November')
plt.xlabel('Exchange Rates')
plt.ylabel('Frequency')
plt.savefig('graphs/ten_months_hist2023.pdf')
plt.show()
