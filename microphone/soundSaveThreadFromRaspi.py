# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:28:29 2020

@author: MarkkuLeino


@reboot /usr/bin/python3 /home/pi/soundSaveThread.py & > /home/pi/logPy.txt



"""

#!/usr/bin/env python3

import pyaudio
#import wave
import multiprocessing
import numpy as np
#import pickle #Not good for np arrays
import time


audio = pyaudio.PyAudio() # create pyaudio instantiation

info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print( "Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name') )



form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 10 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file


# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)

print("recording")
frames = []

#
# 1. thread to analyze (do the FFT) and save the data
#

def saveFFT(data, name):
        N = data.size
        Nper2 = int(N/2)-1
        fourier = np.fft.fft( data/32768.0 )[0:Nper2]

        #print(N)


        #print( sum(abs(fourier)))

        np.save( '/home/pi/fft/'+name+'.npy', fourier )
        #np.save( '/home/pi/fft/data'+name+'.npy', data )
        #with open( name+'.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        #       pickle.dump(fourier, f, protocol=-1)


#
# 2. Main loop to listen the mic and start thread (if possible)
#

while True:
        # loop through stream and append audio chunks to frame array
        startTime = time.strftime("%Y%m%d-%H%M%S")
        frames = []
        for ii in range(0,int((samp_rate/chunk)*record_secs)):
                data = stream.read(chunk, exception_on_overflow = False)
                frames.append(data)

        npdata = np.frombuffer(data, dtype=np.int16)/32768.0
        #print( sum(  abs( npdata ) ) )
        #print( npdata.size )
        p = multiprocessing.Process( target=saveFFT, args=[npdata, startTime]  )
        p.start()

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

