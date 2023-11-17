import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import akshare as ak
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.datasets import co2

exchange_rate_orign_2023df = ak.currency_boc_sina(symbol="加拿大元", start_date="20230101", end_date="20231115")
# Select data which I interested in and rename the columns of dataframe
exchange_rates_2023 = exchange_rate_orign_2023df[['日期','中行钞卖价/汇卖价', '中行汇买价']].rename(
        columns={
            "日期": "date", # type: datetime.dat
            "中行钞卖价/汇卖价": "bank_selling_exchange_rate", # The amount of Chinese currency that Bank of China willing to sell 100 CAD$ to you
            '中行汇买价':"bank_buying_exchange_rate" # The amount of Chinese currency that Bank of China is willing to buy 100 CAD$ from you
            }
        )


# load 2023 exchange rates data
data = exchange_rates_2023.set_index(exchange_rates_2023['date'])

# set up the time series, change index to Timestamp(for resampling)
ts = data['bank_buying_exchange_rate']
ts.index = pd.to_datetime(ts.index)
ts = ts.asfreq('B')

# Plot the time series data
ts.plot(figsize=(12, 6), label='Original Time Series')
plt.legend()
plt.show()

# Define ARIMA model

p, d, q = 4, 3, 1
model = ARIMA(ts, order=(p, d, q))

# Fit the model
results = model.fit()

# Forecast future values
forecast_steps = 5
forecast = results.get_forecast(steps=forecast_steps)

# Extract forecasted values and confidence intervals
forecast_values = forecast.predicted_mean
ci = forecast.conf_int()

# Create a new date range for the forecast period
forecast_date_rng = pd.date_range(start=ts.index[-1], periods=forecast_steps + 1, freq='B')[1:]

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(ts, label='Original Time Series')
plt.plot(forecast_date_rng, forecast_values, label='Forecast')
plt.fill_between(forecast_date_rng, ci.iloc[:, 0], ci.iloc[:, 1], color='gray', alpha=0.3, label='Confidence Interval')
plt.title(f'ARIMA Forecasting_{p}_{d}_{q}')
plt.legend()
plt.savefig(f'arima_para_{p}_{d}_{q}.pdf')
plt.show()
