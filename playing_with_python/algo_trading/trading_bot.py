import packages.modules as simple_functions
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


ema_account = simple_functions.Trading_account(10000)
ema_bollinger_account = simple_functions.Trading_account(10000)

ticker = "BTC-USD"
initial_date = dt.datetime(2015, 4, 1)
finish_date = dt.datetime(2022, 1, 1)

chart = simple_functions.get_chart(ticker, initial_date, finish_date)
chart_volume_profile = simple_functions.volume_profile(chart["Close"], chart["Volume"], 100)

chart["ema_20"] = chart["Close"].ewm(20, adjust=False).mean()
chart["ema_50"] = chart["Close"].ewm(50, adjust=False).mean()

account_worth_chart_only_ema = []
account_worth_chart_ema_bollinger = []
bollinger_bands = simple_functions.get_bollinger_bands(chart["Close"])
chart["upper_band"] = bollinger_bands[0]
chart["lower_band"] = bollinger_bands[1]


for i in range(len(chart["Close"])):
    account_worth_chart_only_ema.append(ema_account.account_value(chart["Close"][i]))
    account_worth_chart_ema_bollinger.append(ema_bollinger_account.account_value(chart["Close"][i]))

    switch_ema_price = chart["Close"][i] >= chart["ema_20"][i]
    if i == 0:
        old_switch_ema_price = switch_ema_price
    if switch_ema_price and not old_switch_ema_price:
        ema_account.trade_asset(chart["Close"][i], (ema_account.actual_stats(0)/10)/chart["Close"][i])

    elif not switch_ema_price and old_switch_ema_price:
        ema_account.trade_asset(chart["Close"][i], -ema_account.actual_stats(1))

    if switch_ema_price and not old_switch_ema_price or chart["Close"][i] <= chart["lower_band"][i]:
        ema_bollinger_account.trade_asset(chart["Close"][i], (ema_bollinger_account.actual_stats(0)/10)/chart["Close"][i])

    elif not switch_ema_price and old_switch_ema_price or chart["Close"][i] >= chart["upper_band"][i]:
        
        ema_bollinger_account.trade_asset(chart["Close"][i], -ema_bollinger_account.actual_stats(1))


    old_switch_ema_price = switch_ema_price
    


chart["20_ema_account"] = account_worth_chart_only_ema
chart["bollinger_ema_account"] = account_worth_chart_ema_bollinger

fig, ((aa, ab), (ac, ad)) = plt.subplots(2, 2, gridspec_kw={"width_ratios":[1,5], "height_ratios":[5,1]})

aa.plot(chart_volume_profile[0], chart_volume_profile[1])
ab.plot(chart[["Close", "upper_band", "lower_band"]])
ac.plot(chart[["20_ema_account", "bollinger_ema_account"]])
ad.plot(chart["Volume"])
plt.show()
print(ema_account.account_performance(chart["Close"][len(chart["Close"])-1]))