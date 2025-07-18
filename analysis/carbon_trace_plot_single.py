import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('xtick', labelsize=24) 
matplotlib.rc('ytick', labelsize=24)

# Load the file
BE = pd.read_parquet("carbon_traces/BE_2022_hourly.parquet")
NL = pd.read_parquet("carbon_traces/NL_2022_hourly.parquet")
DE = pd.read_parquet("carbon_traces/DE_2022_hourly.parquet")
FR = pd.read_parquet("carbon_traces/FR_2022_hourly.parquet")

# Display the first few rows
BE['timestamp'] = pd.to_datetime(BE['timestamp'], unit='ms')
NL['timestamp'] = pd.to_datetime(NL['timestamp'], unit='ms')
DE['timestamp'] = pd.to_datetime(DE['timestamp'], unit='ms')
FR['timestamp'] = pd.to_datetime(FR['timestamp'], unit='ms')

BE.set_index('timestamp', inplace=True)
NL.set_index('timestamp', inplace=True)
DE.set_index('timestamp', inplace=True)
FR.set_index('timestamp', inplace=True)

BE_October_2022 = BE['2022-10-01':'2022-10-31']
NL_October_2022 = NL['2022-10-01':'2022-10-02']
DE_October_2022 = DE['2022-10-01':'2022-10-31']
FR_October_2022 = FR['2022-10-01':'2022-10-31']

plt.figure(figsize=(17, 8))
plt.plot(NL_October_2022.index, NL_October_2022['carbon_intensity'], label='Netherlands', linestyle='-')
plt.title('Carbon Intensity in October 2022 - Netherlands', fontsize=30)
plt.xlabel('Date',fontsize=30)
plt.ylabel('Carbon Intensity (gCO2/kWh)',fontsize=30)
plt.grid(True)
plt.legend(fontsize=30)
plt.ylim(bottom=min(0, plt.ylim()[0]), top=plt.ylim()[1])
plt.tight_layout()
plt.savefig("carbon_trace_october_NL_2022.png")
