import packages.modules as simple_functions
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


def simple_ema_bot(price, ema, account_balance, account_assets, counter, old_ema_price):
    price_over_ema = price >= ema

    if counter==0:
        old_price_over_ema = price_over_ema
    
    else:
        old_price_over_ema = old_ema_price

    if price_over_ema and not old_price_over_ema:
        return [price, (account_balance/10)/price, price_over_ema]

    elif not price_over_ema and old_price_over_ema:
        return [price, -account_assets, price_over_ema]

    else:
        return [price, 0, price_over_ema]