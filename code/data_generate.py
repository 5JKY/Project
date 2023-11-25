import akshare as ak
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


mpl.rcParams.update({
    'figure.figsize': [15, 8]
})

# obtain the exchage rate data from AKShare, which is an elegant and simple financial data interface library for Python
# using the API below, to access history trading data from the following website
# http://biz.finance.sina.com.cn/forex/forex.php?startdate=2012-01-01&enddate=2021-06-14&money_code=EUR&type=0
exchange_rate_orign_df = ak.currency_boc_sina(symbol="加拿大元", start_date="20190101", end_date="20231031")

# Select data which I interested in and rename the columns of dataframe
exchange_rates = exchange_rate_orign_df[['日期','中行钞卖价/汇卖价', '中行汇买价']].rename(
        columns={
            "日期": "date", # type: datetime.date
            "中行钞卖价/汇卖价": "bank_selling_exchange_rate", # The amount of Chinese currency that Bank of China willing to sell 100 CAD$ to you
            '中行汇买价':"bank_buying_exchange_rate" # The amount of Chinese currency that Bank of China is willing to buy 100 CAD$ from you
            }
        )

exchange_rates.set_index(exchange_rates['date'], inplace=True)

# Only care about bank selling exchange rates
selling_rates = exchange_rates['bank_selling_exchange_rate']

# Convert the index to Timestamp for further manipulating
selling_rates.index = pd.to_datetime(selling_rates.index)

selling_rates.plot(alpha=0.3, style='-', label = 'Every Forex Trading Day-orignal data plot')
selling_rates.asfreq('BMS').plot(style='--', label='Sample the Start of Each Month')
selling_rates.asfreq('BYS').plot(style='--', label='Sample the Start of Each Year')

plt.title("CAD/CNY exchange rate trends from 2019 to 2023")
plt.xlabel('Date')
plt.ylabel('Bank Selling Exchange Rate')
plt.legend()
plt.savefig('graphs/forex_trading_rates.pdf')
plt.show()

