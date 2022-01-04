import packages.modules as simple_functions
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

ticker = "BCH-USD"
initial_date = dt.datetime(2015, 1, 1)
finish_date = dt.datetime(2022, 1, 1)

chart = simple_functions.get_chart(ticker, initial_date, finish_date)
chart_volume_profile = simple_functions.volume_profile(chart["Close"], chart["Volume"], 100)


fig, ((aa, ab), (ac, ad)) = plt.subplots(2, 2, gridspec_kw={"width_ratios":[1,5], "height_ratios":[5,1]})

aa.plot(chart_volume_profile[0], chart_volume_profile[1])
ab.plot(chart["Close"])
ad.plot(chart["Volume"])
plt.show()