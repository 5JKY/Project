# Project
Analyze the Canadian Dollar (CAD) to Chinese currency (CNY) exchange rate from 2019 to 2023

## Code and Graphs

All the code needed for the project is stored in the "code" directory. Graphs generated from the code are saved in the "graphs" directory. 
The main scripts and graphs are:

- `code/data_generate.py`: Run this script will generat the exchange rate data, which will be imported by other scripts. The following graphs corresponding to figures in project will also be shown and saved: 
  - `forex_trading_rates.pdf`-> [Figure 1: CAD/CNY Exchange Rates from 2019 to October 2023]
  - `selling_rates.pdf`-> [Figure 2: Bank Selling Exchange Rates Over Time]

- `code/yearly_analysis.py`: Run this script for display and save following graphs corresponding to figures in project: 
  - `yearly_analysis.pdf`-> [Figure 3: Mean, Median, and Extreme Value of Exchange rate on a yearly basis.]
  - `daily_rates_with_yearly_mean.pdf`-> [Figure 4: Display Yearly Mean Value on Original Exchange Rate Data]
    
- `code/histogram_kde.py`: Run this script for display and save following graphs corresponding to figures in project: 
  - `overall_hist.pdf`-> [Figure 5(a): Histogram with KDE for the observed period (from 2019to October 2023)]
  - `subplot_yearly_hist.pdf`-> [Figure 5(c): Histogram with KDE for 4 Different years (from 2019 to 2022)]
  - `ten_months_hist2023.pdf`-> [Figure 5(b): Histogram with KDE for 2023 (from 1st January to 31st October)]

- `code/distribution_scales.py`: Run this script for display and save following graphs corresponding to figures in project: 
  - `std_scales.pdf`-> [Figure 6: Standard Deviation of Exchange Rates at Different Time Frequencies]
  - `distribution_quaterly.pdf`-> [Figure 7: Quarterly Trends in Mean and Extreme Values]
  - `distribution_monthly.pdf`-> [Figure 8: Monthly Trends in Mean and Extreme Values]

- `code/distribution_scales.py`: Run this script for display and save following graphs corresponding to figures in project: 
  - `yearly_MA.pdf`-> [Figure 9: Discrepancy Between 12-Month Moving Average and the Monthly Mean Exchange Rate]
  - `quarterly_MA.pdf`-> This graph has not been choosen for project.

 - `code/seasonality_yearly.py`: Run this script for display and save following graphs corresponding to figures in project: 
    - `seasonal_decompose_yearly.pdf`-> [Figure 10: Seasonal Decomposition of Monthly Mean Exchange Rate (Additive Model)]

- `code/seasonality_quarterly.py`: This script generate `graphs/seasonal_decompose_quarterly.pdf`, which has not been choosen for project.
