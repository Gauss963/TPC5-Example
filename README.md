# TPC5 Example

## Overview

This repository includes two Python scripts designed to read and process data stored in a TPC5 file format. The TPC5 format (as generated by Elsys AG measurement instruments) is HDF5-based, and these scripts utilize the `h5py` library to access and extract measurement data, scaling parameters, and metadata. Once extracted, the data can be visualized or further analyzed.

- **tpc5.py**: A helper module containing functions to:
  - Retrieve dataset names and paths within the HDF5 file.
  - Extract raw and physical voltage data from specified channels and blocks.
  - Access channel names, physical units, sampling rates, trigger times, and recording start times.

- **load_data.py**: An example script demonstrating how to:
  - Open a TPC5 file.
  - Read data from multiple blocks of a specific channel.
  - Extract associated metadata (e.g., trigger time, sampling rate, start time).
  - Plot the results using `matplotlib`.

## File Descriptions

### tpc5.py

This file provides helper functions that encapsulate the logic needed to navigate and interpret the structure of a TPC5 file. The key functions include:

- **`getDataSetName(channel, block=1)`**  
  Returns the HDF5 dataset name for a given channel and block.

- **`getChannelGroupName(channel)`**  
  Returns the HDF5 group path associated with a given channel.

- **`getBlockName(channel, block)`**  
  Returns the group path for a specific block of a given channel.

- **`getVoltageData(fileRef, channel, block=1)`**  
  Retrieves the raw data for the specified channel/block, applies the analog mask, and converts the binary data to voltage using the provided scaling factors.

- **`getPhysicalData(fileRef, channel, block=1)`**  
  Similar to `getVoltageData`, but further converts voltage values into physical units using additional scaling factors.

- **`getChannelName(fileRef, channel)`**  
  Returns the channel name (a string) stored in the file’s attributes.

- **`getPhysicalUnit(fileRef, channel)`**  
  Returns the physical unit (e.g., Volts) associated with the channel data.

- **`getSampleRate(fileRef, channel, block=1)`**  
  Returns the sampling rate in Hertz for a given channel/block.

- **`getTriggerSample(fileRef, channel, block=1)`**  
  Returns the trigger sample index for the specified block, useful for time alignment.

- **`getTriggerTime(fileRef, channel, block=1)`**  
  Returns the trigger time in seconds, giving an absolute time reference.

- **`getStartTime(fileRef, channel, block=1)`**  
  Returns the start time as a string (`YYYY-MM-DDTHH:MM:SS.sss...`) for the recording of a specific block.

The functions above are just wrapped methods. You can define your own methods.

### load_data.py

This is an example usage script that:
1. Opens a TPC5 file named `triggered_test.tpc5`.
2. Reads channel 1 across multiple blocks (in this example, blocks 1 through 4).
3. For each block, extracts:
   - The voltage data array.
   - Trigger time, trigger sample, sampling rate, and start time.
4. Computes the time axis relative to the trigger event and plots the data using `matplotlib`.
5. Closes the file and displays the resulting figure.

## Requirements

- **Python**: Tested with Python 3.x.
- **Packages**:
  - `h5py` (to read HDF5/TPC5 files)
  - `numpy` (for numerical operations)
  - `matplotlib` (for plotting)

You can install the required packages using:
```bash
pip install h5py numpy matplotlib
```

and run the example by
```bash
python3 ./load_data.py
```