import packages.modules as simple_functions
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


def variable_cross(price, variable_1, variable_2, account_balance, account_assets, counter, old_ema_price):
    variable_cross = variable_1 >= variable_2

    if counter==0:
        old_variable_cross = variable_cross
    
    else:
        old_variable_cross = old_ema_price

    if variable_cross and not old_variable_cross:
        return [price, (account_balance)/price, variable_cross]

    elif not variable_cross and old_variable_cross:
        return [price, -account_assets, variable_cross]

    else:
        return [price, 0, variable_cross]

