## @package Analyza_001
#  Documentation for this module.
#
#  More details.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INDIR  = r'..\ODDopravaPK-work_data\in\DOPR_D_20180412'
OUTDIR = r'..\ODDopravaPK-work_data\out\DOPR_D_20180412'

def readDataFrame(path_to_file):
    ## Documentation for a function.
    #
    #  Returns a DataFrame constructed from data in the text file.
    return pd.read_table(path_to_file, sep='|', low_memory=False)

def saveHistogram(file_name, values, title='Title', ylabel='YLabel', xlabel='XLabel', bins=np.arange(start=1, stop=151, step=5), figsize=(10.7,7.3)):
    ## Create and save histogram..
    #
    #  Selects data corresponding to specified devices and vehicle class.
    #  Generates a histogram of speed measurement based on selection.
    values.plot.hist(bins,figsize)
    plt.yscale('log', nonposy='clip')

    plt.ylabel("Qty")
    plt.xlabel("Speed [km/h]")
    plt.title(title)

    plt.savefig(file_name)
    plt.close()


def histDevIDVehType(df, list_of_devices, vehicle_type, title):
    ## Generate Speed histogram for particulat device class from specified vehicle clases.
    #
    #  Selects data corresponding to specified devices and vehicle class.
    #  Generates a histogram of speed measurement based on selection.
    #
    # Reference: https://erikrood.com/Python_References/rows_cols_python.html
    print('-------------------------------------------------------------------')
    print('Analysis DOPR_D - Selecting relevant records.')

    valid = df.loc[df['Stav'] != 1]     # In actual data as of today are all records with Stav=0 (conflict with documentation)
    devices = valid.loc[valid['IdDetektor'].isin(list_of_devices)]
    vehicles = devices.loc[devices['TypVozidla'] == vehicle_type]
    values = vehicles["Rychlost"]
    print('Analysis DOPR_D - Relevant records selected.')

    if len(values) > 0:
        print('Analysis DOPR_D - Ready to plot the histogram.')

#        values.plot.hist(bins=np.arange(start=1, stop=151, step=5),figsize=(10.7,7.3))
#        plt.yscale('log', nonposy='clip')

#        plt.ylabel("Qty")
#        plt.xlabel("Speed [km/h]")
#        plt.title(title)

#        plt.savefig(OUTDIR + r'\\' + title + '_Rychlost.png')
#        plt.close()

        saveHistogram(OUTDIR + r'\\' + title + '_Rychlost.png', values, title=title, ylabel="Qty", xlabel="Speed [km/h]")

        print('Analysis DOPR_D - Histogram stored.')
    else:
        print('Analysis DOPR_D - No values left to plot the histogram.')

#
# Main code
#
print('Analysis DOPR_D - Start.')

df01 = readDataFrame(INDIR + r'\DOPR_D_20180412_final.csv')

print('Analysis DOPR_D - Dataframe import finished.')

# Bike
histDevIDVehType(df01, ['10059001', '10059101' ,'10059201'], 1, 'Bike')
# Car
histDevIDVehType(df01, ['10059001', '10059101' ,'10059201'], 2, 'Car')
# Van
histDevIDVehType(df01, ['10059001', '10059101' ,'10059201'], 3, 'Van')
# Truck
histDevIDVehType(df01, ['10059001', '10059101' ,'10059201'], 4, 'Truck')

print('-------------------------------------------------------------------')
print('Analysis DOPR_D - Finished.')

#
# STOUPA
#
#
