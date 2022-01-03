import random as rd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


how_many_days = 100000
initial_price = 100
day = []
price = []
volume = []
volume_profile = []

probabilty_volume = []

for i in range(200):
    if i+1 <= 50:
        for d in range((i+1)**2):
            probabilty_volume.append(i+1)
    else:
        for d in range(int((2500/((i+1)**(6/5)))**(2.3))):
            probabilty_volume.append(i+1)

for i in range(how_many_days):
    day.append(i)
    price_change = rd.randint(500, 1000)

    if rd.randint(0,1) == 0:
        initial_price -= initial_price/price_change
    else:
        initial_price += initial_price/price_change

    price.append(initial_price)

for i in range(how_many_days):
    volume.append(probabilty_volume[rd.randint(0, len(probabilty_volume)-1)])

volume_profile = []

for i in range(len(price)):
     for d in range(volume[i]):
         volume_profile.append(price[i])

fig, ((aa, ab), (ac, ad)) = plt.subplots(2,2, gridspec_kw={"width_ratios": [1,5], "height_ratios":[5,1]})

price_data_frame = pd.DataFrame(price, day)
aa.hist(volume_profile, 30, orientation="horizontal", label="Volume Profile")
plt.legend()
ab.plot(price_data_frame, label="Price")
ab.plot(price_data_frame.ewm(100, adjust=False).mean(), label="100 EMA")
plt.legend()
ac.hist(volume, 20, orientation="horizontal")
plt.legend()
ad.bar(day, volume, label="Volume")
plt.legend()
plt.show()