import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import csv
from numpy import ma
from matplotlib.dates import strpdate2num

def readfiles(file_list,c1):
    """ read <TAB> delemited files as strings
        ignoring '# Comment' lines """
    data = []
    for fname in file_list:
        data.append(
                    np.loadtxt(fname,
                               usecols=(0,c1),
                               comments='#',    # skip comment lines
                               delimiter='\t',
                               converters = { 0 : strpdate2num('%Y-%m-%d %H:%M:%S') },
                               dtype=None))
    return data

def init_plot(title, yMin=-0, yMax=18):
    plt.figure(figsize=(24, 12))
    plt.title(title + disclamers)
    plt.xlabel(xtext)
    plt.ylabel(ytext)
    plt.ylim(yMin,yMax)
    plt.grid()

def end_plot(name=None, cols=5):
    plt.legend(bbox_to_anchor=(0, -.1, 1, -0.5), loc=8, ncol=cols,
               mode="expand", borderaxespad=-1.,  scatterpoints=1)
    if name:
        plt.savefig(name, bbox_inches='tight')

disclamers = ('\nUSGS PROVISIONAL DATA'
              '\nSUBJECT TO REVISION'
              )
xtext = ('Date & Time')
ytext = ('Battery Voltage')

data = readfiles(['waMVD116_14d.txt'],2)
data_1 = ma.fix_invalid(data, fill_value = 'nan')
column_0_MVD116 = np.array(data_1)[0][:,0]
battery_volt_MVD116 = np.array(data_1)[0][:,1]

data = readfiles(['waWatertonA_14d.txt'],2)
data_1 = ma.fix_invalid(data, fill_value = 'nan')
column_0_MWatA= np.array(data_1)[0][:,0]
battery_volt_MWatA = np.array(data_1)[0][:,1]

data = readfiles(['waWatertonB_14d.txt'],2)
data_1 = ma.fix_invalid(data, fill_value = 'nan')
column_0_MWatB = np.array(data_1)[0][:,0]
battery_volt_MWatB = np.array(data_1)[0][:,1]

data = readfiles(['waMWWD_14d.txt'],2)
data_1 = ma.fix_invalid(data, fill_value = 'nan')
column_0_MWWD = np.array(data_1)[0][:,0]
battery_volt_MWWD = np.array(data_1)[0][:,1]

data = readfiles(['waMLP_14d.txt'],2)
data_1 = ma.fix_invalid(data, fill_value = 'nan')
column_0_MLP = np.array(data_1)[0][:,0]
battery_volt_MLP = np.array(data_1)[0][:,1]


init_plot('Battery voltage at all Stations')

plt.plot(column_0_MVD116, battery_volt_MVD116, linestyle='-', color='b', label='MVD & 116 St SW')
plt.plot(column_0_MWatA, battery_volt_MWatA, linestyle='-', color='r', label='Waterton Cir. A')
plt.plot(column_0_MVD116, battery_volt_MVD116, linestyle='-', color='g', label='Waterton Cir. B')
plt.plot(column_0_MVD116, battery_volt_MVD116, linestyle='-', color='c', label='MWWD')
plt.plot(column_0_MVD116, battery_volt_MVD116, linestyle='-', color='m', label='MLP')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator())
plt.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=6))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

end_plot(name='M_battery.png')

# ------------------------

#data = readfiles(['waMLP_14d.txt'],4)
#data_1 = ma.fix_invalid(data, fill_value = 'nan')
#
#column_0 = np.array(data_1)[0][:,0]
#airTempRaw = np.array(data_1)[0][:,1]
#
##Compute Air Temperature
#airTempRs_ohms = 23100*((airTempRaw/2500)/(1-(airTempRaw/2500))) # use for CR200 series
##airTempRs_ohms = 23100*(airTempRaw/(1-airTempRaw)) # use for CR1000
#airTemp_degC = -39.17*np.log(airTempRs_ohms) + 410.43
#airTemp_degF = 9.*airTemp_degC/5. +32.
#
#init_plot('Air Temperature at Mukilteo Lighthouse Park')
#
##plt.plot(column_0, airTemp_degC, linestyle='-', color='b', label='Air Temperature')
#plt.plot(column_0, airTemp_degF, linestyle='-', color='b', label='Air Temperature')
#
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.HourLocator())
#plt.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=6))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
#
#end_plot(name='MLP_airTemp.png')

# ------------------------

#data = readfiles(['waMWWD_14d.txt'],4)
#data_1 = ma.fix_invalid(data, fill_value = 'nan')
#
#column_0 = np.array(data_1)[0][:,0]
#airTempRaw = np.array(data_1)[0][:,1]
#
##Compute Air Temperature
#airTempRs_ohms = 23100*((airTempRaw/2500)/(1-(airTempRaw/2500))) # use for CR200 series
##airTempRs_ohms = 23100*(airTempRaw/(1-airTempRaw)) # use for CR1000
#airTemp_degC = -39.17*np.log(airTempRs_ohms) + 410.43
#airTemp_degF = 9.*airTemp_degC/5. +32.
#
#init_plot('Air Temperature at Mukilteo Wastewater Plant')
#
##plt.plot(column_0, airTemp_degC, linestyle='-', color='b', label='Air Temperature')
#plt.plot(column_0, airTemp_degF, linestyle='-', color='b', label='Air Temperature')
#
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.HourLocator())
#plt.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=6))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
#
#end_plot(name='MWWD_airTemp.png')

# ------------------------

#data = readfiles(['waWatertonA_14d.txt'],4)
#data_1 = ma.fix_invalid(data, fill_value = 'nan')
#
#column_0 = np.array(data_1)[0][:,0]
#airTempRaw = np.array(data_1)[0][:,1]
#
##Compute Air Temperature
## airTempRs_ohms = 23100*((airTempRaw/2500)/(1-(airTempRaw/2500))) # use for CR200 series
#airTempRs_ohms = 23100*(airTempRaw/(1-airTempRaw)) # use for CR1000
#airTemp_degC = -39.17*np.log(airTempRs_ohms) + 410.43
#airTemp_degF = 9.*airTemp_degC/5. +32.
#
#init_plot('Air Temperature at Waterton Circle Station A')
#
##plt.plot(column_0, airTemp_degC, linestyle='-', color='b', label='Air Temperature')
#plt.plot(column_0, airTemp_degF, linestyle='-', color='b', label='Air Temperature')
#
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d\n%H:%M'))
#plt.gca().xaxis.set_major_locator(mdates.HourLocator())
#plt.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=6))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

# end_plot(name='MWat_airTemp.png')