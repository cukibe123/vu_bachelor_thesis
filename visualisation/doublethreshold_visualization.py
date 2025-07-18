import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Patch
import matplotlib

FR = pd.read_parquet("carbon_traces/FR_2022_hourly.parquet")

# Display the first few rows
FR['timestamp'] = pd.to_datetime(FR['timestamp'], unit='ms')
FR.set_index('timestamp', inplace=True)
FR_October_2022 = FR['2022-10-01':'2022-10-02']
my_fontsize=16
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)

sorted = sorted(FR_October_2022['carbon_intensity'])

upper_threshold = sorted[int(len(sorted) * 0.6)]
lower_threshold = sorted[int(len(sorted) * 0.3)]

plt.figure(figsize=(12, 6))
plt.plot(FR_October_2022.index, FR_October_2022['carbon_intensity'], label='France', linestyle='--', color='black')

# # Shade the upper region (above threshold)
plt.axhspan(upper_threshold, FR_October_2022['carbon_intensity'].max(),
            facecolor='none', hatch="//", alpha=1)

# # Shade the lower region (below threshold)
plt.axhspan(FR_October_2022['carbon_intensity'].min(), lower_threshold,
            facecolor='none', hatch=".",alpha=1)

upper_patch = Patch(facecolor='none', edgecolor='black', hatch='//', label='Tasks are interrupted')
lower_patch = Patch(facecolor='none', edgecolor='black', hatch='..', label='Tasks are running')
free_patch = Patch(facecolor='none', edgecolor='black', hatch='', label='Tasks remain their current states')

# Draw a horizontal dashed line at the upper threshold
plt.axhline(y=upper_threshold, color='black', linestyle='-', linewidth=2, label='Upper Threshold')
# Draw a horizontal dashed line at the lower threshold
plt.axhline(y=lower_threshold, color='black', linestyle='-.', linewidth=2, label='Lower Threshold')

plt.title('Carbon Intensity in the first two days of October 2022', fontsize=my_fontsize)
plt.xlabel('Days and Hours', fontsize=my_fontsize)
plt.ylabel('Carbon Intensity (gCO2/kWh)', fontsize=my_fontsize)
plt.grid(True)


handles, labels = plt.gca().get_legend_handles_labels()

# Add legend
handles.append(upper_patch)
labels.append('Tasks are interrupted')

handles.append(lower_patch)
labels.append('Tasks are running')

handles.append(upper_patch)
labels.append('Tasks are interrupted')

handles.append(free_patch)
labels.append('Tasks remain current states')

plt.legend(handles=handles, labels=labels, fontsize=my_fontsize)

plt.tight_layout()
plt.savefig("doublethreshold_visualization.pdf")

