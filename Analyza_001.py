import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INDIR  = r'DOPR_D_20180412'
OUTDIR = r'DOPR_D_20180412-out'

def readDataFrame(path_to_file):
    return pd.read_table(path_to_file, sep='|', low_memory=False)

def generateHistogram(df,vehicle, title):
    valid = df01.loc[df01['Stav'] != 1]
    trucks = valid.loc[df01['TypVozidla'] == vehicle]
    values = trucks["Rychlost"]
    values.plot.hist(bins=np.arange(start=1, stop=151, step=5),figsize=(10.7,7.3))
    plt.yscale('log', nonposy='clip')

    plt.ylabel("Qty")
    plt.xlabel("Speed [km/h]")
    plt.title(title)

    print('Analysis DOPR_D - Ready to plot the histogram')
    plt.savefig(OUTDIR + r'\\' + title + '_Rychlost.png')
    plt.close()

    print('Analysis DOPR_D - Finished')
    print('-------------------------------------------------------------------')

#
# Main code
#
print('Analysis DOPR_D - Start')
print('Analysis DOPR_D - Dataframe import finished')
df01 = readDataFrame(INDIR + r'\DOPR_D_20180412_final.csv')

# Bike
#generateHistogram(df01, 1, 'Bike')
# Car
generateHistogram(df01, 2, 'Car')
# Van
generateHistogram(df01, 3, 'Van')
# Truck
generateHistogram(df01, 4, 'Truck')

#
# STOUPA
#
#
#from scipy import signal

def designFilter():
    return sc.signal.firls(9, [0, 2000, 2100, 2200, 3000], [1.0, 1.0, 0.25, 0.125, 0])

def simulateFilter(df01):
    Fs = 4000;  # sampling rate
    Ts = 1.0/Fs; # sampling interval
    time = df01['time']
    value = df01['adc1Value_DEC'] - 2047
    #value = df01['adc2Value_DEC'] - 2047

    #n = len(value) # length of the signal
    n = 8000 # length of the signal
    k = np.arange(n)
    #T = n/Fs
    T = 2
    frq = k//T # two sides frequency range
    frq = frq[range(n//2)] # one side frequency range

    b, a = signal.butter(21, 0.5)
    y = signal.filtfilt(b, a, value)

    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(n//2)]

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(time,value)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(time,y)
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Amplitude')
    #ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
    #ax[1].set_xlabel('Freq (Hz)')
    #ax[1].set_ylabel('|Y(freq)|')

#df01['adc1Value_DEC'].plot()

#df01['Pace'].plot.hist(bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#out = pd.cut(df01['adc1Value_DEC'], bins=[0, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 10], include_lowest=True)

#out_norm = out.value_counts(sort=False, normalize=True).mul(100)

#ax = out_norm.plot.bar(rot=0, color="b", figsize=(6,4))

#ax.set_xticklabels([c[1:-1].replace(","," to") for c in out.cat.categories])
