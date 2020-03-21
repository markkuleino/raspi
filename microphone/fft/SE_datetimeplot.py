# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 10:01:44 2020

@author: MarkkuLeino
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Define time range with 12 different days:
a = datetime.datetime.today()
x_data = [a - datetime.timedelta(hours=x) for x in range(26) ]
# Check how this dates looks like:
print(x_data)
y_data = np.random.rand(26)
fig, ax = plt.subplots()
ax.plot(x_data, y_data)
# Make ticks on occurrences of each month:
ax.xaxis.set_major_locator(mdates.HourLocator())
# Get only the month to show in the x-axis:
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
# '%b' means month as locale’s abbreviated name
plt.show()



"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Define time range with 12 different days:
a = datetime.datetime.today()
x_data = [a - datetime.timedelta(days=x) for x in range(12) ]
# Check how this dates looks like:
print(x_data)
y_data = np.random.rand(12)
fig, ax = plt.subplots()
ax.plot(x_data, y_data)
# Make ticks on occurrences of each month:
ax.xaxis.set_major_locator(mdates.DayLocator())
# Get only the month to show in the x-axis:
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
# '%b' means month as locale’s abbreviated name
plt.show()

"""

"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

# Define time range with 12 different months:
# `MS` stands for month start frequency 
x_data = pd.date_range('2018-01-01', periods=12, freq='MS') 
# Check how this dates looks like:
print(x_data)
y_data = np.random.rand(12)
fig, ax = plt.subplots()
ax.plot(x_data, y_data)
# Make ticks on occurrences of each month:
ax.xaxis.set_major_locator(mdates.MonthLocator())
# Get only the month to show in the x-axis:
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
# '%b' means month as locale’s abbreviated name
plt.show()

"""


