''' Python Expample file for data read out from a TPC5 File
    Copyright: 2017 Elsys AG
    
    This example shows how to open a TPC5 file, read out the measurement data
    and the conversion values.
    The TestData.tpc5 contains 12 channels and 1 block per channel.
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt

''' Import Custom Helper Function for reading TPC5 Files '''
import tpc5

filename = './triggered_test.tpc5'


file_instance = h5py.File(filename, "r")

fig = plt.figure()
fig.suptitle('Imported Tpc5 File', fontsize = 14, fontweight = 'bold')
''' Scale x Axis to ms '''
TimeScale = 1

''' Get Data scaled int voltage from channel 1 '''
ch = 1
ch1 = tpc5.getChannelName(file_instance, 1)
unit = f'[ {tpc5.getPhysicalUnit(file_instance, 1)} ]'


for block in range(1, 5):
    data = tpc5.getVoltageData(file_instance, ch, block)
    TriggerTime = tpc5.getTriggerTime(file_instance, 1, block)
    TriggerSample = tpc5.getTriggerSample(file_instance, 1, block)
    SamplingRate  = tpc5.getSampleRate(file_instance, 1, block)
    RecTimeString = tpc5.getStartTime(file_instance, 1, block)
    RecTimeList   = RecTimeString.split('T',1)
    RecDate       = RecTimeList[0]
    TimeListe     = RecTimeList[1].split('.',1)
    RecTime       = TimeListe[0] 


    startTime = -TriggerSample /SamplingRate * TimeScale
    endTime   = (len(data)-TriggerSample)/SamplingRate * TimeScale
    t         = np.arange(startTime, endTime, 1/SamplingRate * TimeScale) + TriggerTime * TimeScale
    print(len(t), len(data))
    if block == 1:
        label = 'complete'
    else:
        label = 'event %d' % (block - 1)
    plt.plot(t, data, label=label)
file_instance.close



plt.legend(framealpha = 0.5)

if TimeScale == 1: 
    plt.xlabel('time (s)')
elif TimeScale == 1000:
    plt.xlabel('time (ms)')
elif TimeScale == 1000000:
    plt.xlabel('time (us)')

plt.ylabel(unit)
plt.title('Recording Time: ' + RecDate + ' ' + RecTime)
plt.grid(True)
plt.tight_layout()
plt.savefig(f'./plot/{filename}_plot.pdf', dpi = 300)
plt.show()