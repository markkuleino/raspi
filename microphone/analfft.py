# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:11:24 2020

@author: MarkkuLeino
"""

from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

import pickle

fs, data = wavfile.read('test1.wav')
plt.subplot(211)
plt.plot( data )




#FFT
# see 
# https://stackoverflow.com/questions/4364823/how-do-i-obtain-the-frequencies-of-each-value-in-an-fft
# for the frequencies

# Each data point is a signed 16 bit number, so we can normalize by dividing 32*1024

N = data.size
Nper2 = int(N/2)-1
fourier = np.fft.fft( data/32768.0 )[0:Nper2]
Fs = 44100
freq = np.fft.fftfreq(N, d=1/Fs)[0:Nper2]

plt.subplot(212)
plt.plot( freq, fourier )

with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(fourier, f, protocol=-1)


