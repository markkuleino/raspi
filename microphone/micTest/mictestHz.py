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

N = (2047)
Fs = 44100
freq = np.arange(N)*Fs/(2*N)  #https://stackoverflow.com/questions/4364823/how-do-i-obtain-the-frequencies-of-each-value-in-an-fft

 
Nfiles = len([name for name in os.listdir('./') if os.path.isfile('./'+name)])
print( Nfiles )

freqMatrix = np.zeros( shape=(N, Nfiles) )



fig = plt.figure()
#ax = fig.add_subplot(111,aspect='equal')

for i, npfile in enumerate( glob.glob("./*.npy") ):
    
    A= np.load( npfile )
    freqMatrix[:,i] = abs( A )

    #print(A.size)
    #if sum(abs(A)) > 0:
    #    print(sum(abs(A)) )
    #    print(A)
    #plt.plot( freq, abs(A) )
    #print(A)

plt.imshow( freqMatrix[:1000,:], cmap='gray_r',  aspect=0.002 )
plt.ylabel( "Frequency" )
plt.xlabel( "Time" )
    