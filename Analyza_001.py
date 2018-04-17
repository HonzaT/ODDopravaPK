import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INDIR  = r'..\ODDopravaPK-work_data\in\DOPR_D_20180412'
OUTDIR = r'..\ODDopravaPK-work_data\out\DOPR_D_20180412'

def readDataFrame(path_to_file):
    return pd.read_table(path_to_file, sep='|', low_memory=False)

def generateHistogram(df, vehicle_type, title):
    valid = df01.loc[df01['Stav'] != 1]
    trucks = valid.loc[df01['TypVozidla'] == vehicle_type]
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

df01 = readDataFrame(INDIR + r'\DOPR_D_20180412_final.csv')

print('Analysis DOPR_D - Dataframe import finished')

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
