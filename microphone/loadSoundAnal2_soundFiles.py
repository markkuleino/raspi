# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:02:41 2020

@author: MarkkuLeino
#https://stackoverflow.com/questions/16819193/choosing-marker-size-in-matplotlib

"""

import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy.io.wavfile import write


for i, npfile in enumerate( glob.glob("fft/data*.npy") ):
    
    A= np.load( npfile )
    print(A.size)

    #print(A.size)
    #if sum(abs(A)) > 0:
    #    print(sum(abs(A)) )
    #    print(A)
    plt.plot( A )
    
    scaled = np.int16(A/np.max(np.abs(A)) * 32767)
    write('test.wav', 44100, scaled)

