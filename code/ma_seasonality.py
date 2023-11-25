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


selling_rates.resample('BMS').mean().rolling(window=12, center=True).mean().plot(style='--', label=f'12 month moving average')
selling_rates.resample('BMS').mean().plot(alpha=0.3, style='-', label = 'Exchange Rates Original Data')

plt.title('Monthly Mean with Moving Average Overlay')
plt.xlabel('Year')
plt.ylabel('Exchange Rate')
plt.legend()
plt.tight_layout()
plt.savefig('graphs/monthly_MA.pdf')
plt.show()


# Perform seasonal decomposition, choose additive model
result = seasonal_decompose(selling_rates.resample('BMS').mean(), model='additive', period=12)

# subplot trend(moving average above), seasonal, residual component
fig, axs = plt.subplots(3, 1, sharex=True)

# Trend component
axs[0].plot(result.trend, label='Trend Component')
axs[0].legend(loc='lower left') 

# Seasonal component
axs[1].plot(result.seasonal, label='Seasonal Component')
axs[1].legend(loc='lower left')

# Residual component
axs[2].plot(result.resid, label='Residual Component')
axs[2].legend(loc='lower left')
plt.tight_layout()
plt.savefig('graphs/seasonal_decompose.pdf')
plt.show()
