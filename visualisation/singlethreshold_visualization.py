import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Patch
import matplotlib

NL = pd.read_parquet("carbon_traces/NL_2022_hourly.parquet")

# Display the first few rows
NL['timestamp'] = pd.to_datetime(NL['timestamp'], unit='ms')
NL.set_index('timestamp', inplace=True)
NL_October_2022 = NL['2022-10-01':'2022-10-02']
my_fontsize=16
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)

plt.figure(figsize=(12, 6))
plt.plot(NL_October_2022.index, NL_October_2022['carbon_intensity'], label='Netherlands', linestyle='--', color='black', linewidth=2)

threshold_value = 250
upper_patch = Patch(facecolor='none', edgecolor='black', hatch='//', label='Tasks are interrupted')
lower_patch = Patch(facecolor='none', edgecolor='black', hatch='..', label='Tasks are running')


# Shade the upper region (above threshold)
plt.axhspan(threshold_value, NL_October_2022['carbon_intensity'].max(),
            facecolor='none', hatch='//', alpha=1)

# Shade the lower region (below threshold)
plt.axhspan(NL_October_2022['carbon_intensity'].min(), threshold_value,
            facecolor='none', hatch='.', alpha=1)


# Draw a horizontal dashed line at the threshold
plt.axhline(y=threshold_value, color='black', linestyle='-', linewidth=3, label="Carbon Threshold")

plt.title('Carbon Intensity in the first two days of October 2022', fontsize=my_fontsize)
plt.xlabel('Days and Hours', fontsize=my_fontsize)
plt.ylabel('Carbon Intensity (gCO2/kWh)', fontsize=my_fontsize)

handles, labels = plt.gca().get_legend_handles_labels()

# Add legend
handles.append(upper_patch)
labels.append('Tasks are interrupted')

handles.append(lower_patch)
labels.append('Tasks are running')

plt.legend(handles=handles, labels=labels, fontsize=my_fontsize)

plt.grid(True)
plt.tight_layout()
plt.savefig("singlethreshold_visualization.pdf")

