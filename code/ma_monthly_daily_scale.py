from data_generate import selling_rates

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from statsmodels.tsa.seasonal import seasonal_decompose

mpl.rcParams.update({
    'figure.figsize': [15, 8]
})

# resample the data to monthly frequency and computes a 12-month centered moving average
selling_rates.resample('BMS').mean().rolling(window=12, center=True).mean().plot(style='--', label='12 month moving average')
selling_rates.resample('BMS').mean().plot(alpha=0.3, style='-', label = 'Monthly Mean Exchange Rate')

plt.title('Monthly Mean Exchange Rate with Yearly Moving Average Overlay')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.tight_layout()
plt.savefig('graphs/yearly_MA.pdf')
plt.show()


# operate MA on the original data with a window size of three months of business days(quarterly)
# assuming an average of 21 business days per month, each quater has three months
window = 21*3
selling_rates.rolling(window, center=True).mean().plot(style='--', label=f'{window} bussine days moving average')
selling_rates.plot(alpha=0.3, style='-', label = 'Daily Exchange Rate-orignal data')

plt.title('Daily Exchange Rate with Quarterly Moving Average Overlay')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.tight_layout()
plt.savefig('graphs/quarterly_MA.pdf')
plt.show()
