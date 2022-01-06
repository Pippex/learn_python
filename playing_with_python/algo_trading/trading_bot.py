import packages.modules as simple_functions
import packages.all_trading_bots as ema_price_bot
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


ema_account = simple_functions.Trading_account(100)
ema_bollinger_account = simple_functions.Trading_account(10000)

ticker = "BTC-USD"
initial_date = dt.datetime(2017, 9, 25)
finish_date = dt.datetime(2022, 1, 1)

chart = simple_functions.get_chart(ticker, initial_date, finish_date)
chart_volume_profile = simple_functions.volume_profile(chart["Close"], chart["Volume"], 100)

chart["ema_20"] = chart["Close"].ewm(20, adjust=False).mean()
chart["ema_50"] = chart["Close"].ewm(50, adjust=False).mean()

account_worth_chart_only_ema = []
bollinger_bands = simple_functions.get_bollinger_bands(chart["Close"])
chart["upper_band"] = bollinger_bands[0]
chart["lower_band"] = bollinger_bands[1]

old_price_over_ema = False

for i in range(len(chart["Close"])):
    ema_account.trade_asset(ema_price_bot.variable_cross(chart["Close"][i], chart["ema_20"][i], chart["ema_50"][i], ema_account.actual_stats(0), ema_account.actual_stats(1), i, old_price_over_ema))
    old_price_over_ema = ema_price_bot.variable_cross(chart["Close"][i], chart["ema_20"][i], chart["ema_50"][i], ema_account.actual_stats(0), ema_account.actual_stats(1), i, old_price_over_ema)[2]
    account_worth_chart_only_ema.append(ema_account.account_value(chart["Close"][i]))


chart["20_ema_account"] = account_worth_chart_only_ema

fig, ((aa, ab), (ac, ad)) = plt.subplots(2, 2, gridspec_kw={"width_ratios":[1,5], "height_ratios":[5,1]})
print(ema_account.account_performance(chart["Close"][len(chart["Close"])-1]))
aa.plot(chart_volume_profile[0], chart_volume_profile[1])
ab.plot(chart[["Close", "upper_band", "lower_band"]])
ac.plot(chart["20_ema_account"])
ad.plot(chart["Volume"])
plt.show()
