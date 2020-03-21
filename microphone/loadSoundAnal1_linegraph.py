# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:02:41 2020

@author: MarkkuLeino
#https://stackoverflow.com/questions/16819193/choosing-marker-size-in-matplotlib

"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os, os.path
from datetime import datetime
import matplotlib.dates as mdates
#import datetime as dt

N = (2047)
Fs = 44100
freq = np.arange(N)*Fs/(N)  #Check this, dude!


directory = 'fft/01_Monday_0113/'
Nfiles = len([name for name in os.listdir(directory) if os.path.isfile(directory+name)])
print( Nfiles )

freqMatrix = np.zeros( shape=(N, Nfiles) )
freqTime = np.zeros(  Nfiles-2, dtype="M8[s]" )

#fig = plt.figure()
fig, ax = plt.subplots()

#ax = fig.add_subplot(111,aspect='equal')


print('Starting')
for i, npfile in enumerate( glob.glob(directory+'*.npy') ):
    
    print( npfile )
    idx = npfile.find('\\')
    #print(idx)
    nptime = npfile[idx+1:-4]
    #print( nptime )
    
    datetime_object = datetime.strptime( nptime,'%Y%m%d-%H%M%S' )

    print(datetime_object)

    A= np.load( npfile )
    freqMatrix[:,i] = abs( A )
    freqTime[i] = datetime_object


#plt.plot( freqMatrix )

#x_lims = [freqTime[0], freqTime[-1]]
#x_lims = mdates.date2num(x_lims)

xt = mdates.date2num( freqTime )


ax.imshow( freqMatrix[:1000,:], cmap='gray_r', vmin=0, vmax=1e-4, aspect='auto' )
#plt.xticks( xt )


ax.set_xticks(np.arange(len(xt)) )
ax.set_xticklabels(xt)
ax.tick_params(length=6)

ax.xaxis_date()
date_format = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(date_format)

# This simply sets the x-axis data to diagonal so it fits better.
#fig.autofmt_xdate()
plt.show()




"""
#Works but the ticks are not correctly set
x_lims = [freqTime[0], freqTime[-4]]
x_lims = mdates.date2num(x_lims)

ax.imshow( freqMatrix[:1000,:], extent=[x_lims[0], x_lims[1], 1000, 0], cmap='gray_r', vmin=0, vmax=1e-4, aspect='auto' )
ax.xaxis_date()
date_format = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(date_format)
# This simply sets the x-axis data to diagonal so it fits better.
fig.autofmt_xdate()
plt.show()
"""


#ax.xaxis.set_ticks(np.arange(start, end, 0.712123))
#ax.xaxis.set_major_locator(mdates.HourLocator())



  