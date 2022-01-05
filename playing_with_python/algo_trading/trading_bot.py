import packages.modules as simple_functions
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


class Trading_account():

    def __init__(self, balance):
        self.__initial_status = [balance, 0]
        self.__actual_status = [balance, 0]


    def trade_asset(self, price, quantity):
        self.__actual_status = simple_functions.trade_asset(self.__actual_status[0], self.__actual_status[1], price, quantity)

    def account_value(self, price):
        return self.__actual_status[0] + price * self.__actual_status[1]


    def account_worth_change(self, price):
        return self.account_value(price)/(self.__initial_status[0]/100)-100


    def actual_stats(self, argument):
        return self.__actual_status[argument]


    def account_performance(self, price):
        print(f"The account started with ${self.__initial_status[0]} \
now the account has ${self.__actual_status[0]} and {self.__actual_status[1]} assets, \
the account is valued in ${self.account_value(price)}, \
is {self.account_worth_change(price)}% up")


ema_account = Trading_account(10000)
ema_cross_account = Trading_account(10000)

ticker = "SPY"
initial_date = dt.datetime(2015, 4, 1)
finish_date = dt.datetime(2022, 1, 1)

chart = simple_functions.get_chart(ticker, initial_date, finish_date)
chart_volume_profile = simple_functions.volume_profile(chart["Close"], chart["Volume"], 100)

chart["ema_20"] = chart["Close"].ewm(20, adjust=False).mean()
chart["ema_50"] = chart["Close"].ewm(50, adjust=False).mean()

for i in range(len(chart["Close"])):

    switch_ema_price = chart["Close"][i] >= chart["ema_20"][i]
    if i == 0:
        old_switch_ema_price = switch_ema_price
    if switch_ema_price and not old_switch_ema_price:
        ema_account.trade_asset(chart["Close"][i], (ema_account.actual_stats(0)/10)/chart["Close"][i])
    
    elif not switch_ema_price and old_switch_ema_price:
        ema_account.trade_asset(chart["Close"][i], -ema_account.actual_stats(1))

    old_switch_ema_price = switch_ema_price


#fig, ((aa, ab), (ac, ad)) = plt.subplots(2, 2, gridspec_kw={"width_ratios":[1,5], "height_ratios":[5,1]})

#aa.plot(chart_volume_profile[0], chart_volume_profile[1])
#ab.plot(chart["Close"])
#ad.plot(chart["Volume"])
#plt.show()
print(ema_account.account_performance(chart["Close"][len(chart["Close"])-1]))