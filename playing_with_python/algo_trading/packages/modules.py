import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime as dt
import random as rd


#This is a simple def only to make more easy the reading of the code
def get_chart(ticker, initial_date, finish_date):
    return web.DataReader(ticker, "yahoo", initial_date, finish_date)


#This is a volume profile creator
def volume_profile(chart, volume, levels):
    higher_high = max(chart)
    lower_low = min(chart)
    level_diference = (higher_high-lower_low)/levels #This is to view if a price is
    #In a level, like 5000-5100 and add one to the counter of this level
    levels_list = []
    
    for i in range(levels):
        levels_list.append(lower_low + (i) * level_diference + level_diference/2) #We will create a DataFrame with 
        #this

    volume_in_level = []

    for i in levels_list:
        volume_in_level.append(0)

    for i in range(len(chart)):
        for d in range(levels):
            if lower_low+d* level_diference <= chart[i] <= lower_low + (d+1) * (level_diference):
                volume_in_level[d] += volume[i]
    
    return [volume_in_level, levels_list]

def random_chart(how_many_days, initial_price, min_movement, max_movement, max_volume):
    day = []
    price = []
    volume = []
    probabilty_volume = []

    for i in range(max_volume):
        if i+1 <= max_volume/4:
            for d in range((i+1)**2):
                probabilty_volume.append(i+1)
        else:
            for d in range(int((max_volume**2/((i+1)**(6/5)))**(2.3))):
                probabilty_volume.append(i+1)

    for i in range(how_many_days):
        day.append(i)
        price_change = rd.randint(min_movement, max_movement)

        if rd.randint(0,1) == 0:
            initial_price -= initial_price/price_change
        else:
            initial_price += initial_price/price_change

        price.append(initial_price)

    for i in range(how_many_days):
        volume.append(probabilty_volume[rd.randint(0, len(probabilty_volume)-1)])

    dataFrame = pd.DataFrame(day)
    dataFrame["Price"] = pd.DataFrame(price)
    dataFrame["Volume"] = pd.DataFrame(volume)
    return dataFrame

