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
plt.plot(NL_October_2022.index, NL_October_2022['carbon_intensity'], label='Netherlands', linestyle='--', color='black')



original_start_time = pd.Timestamp("2022-10-01 0:00")
original_end_time = pd.Timestamp("2022-10-02 23:00")

submitted_time = pd.Timestamp("2022-10-01 5:00")
y_start_1 = 230

y_start_2 = 130

width = pd.Timedelta(hours=3)
height = 20

rect = patches.Rectangle((submitted_time, y_start_1), width, height,
                         linewidth=1, color='black', alpha=1,
                         label='Submitted Task')
plt.gca().add_patch(rect)

start_time = pd.Timestamp("2022-10-01 10:00")
end_time = pd.Timestamp("2022-10-01 13:00")

rect_2 = patches.Rectangle((start_time, y_start_2), width, height,
                         linewidth=1, color='black', alpha=1,
                         )
plt.gca().add_patch(rect_2)

plt.axvspan(original_start_time, start_time,
            facecolor='none', hatch='//', alpha=1)

plt.axvspan(start_time, end_time,
            facecolor='none', hatch='.', alpha=1)

# Draw a vertical line at the deadline
plt.axvline(x=pd.Timestamp("2022-10-02 00:00"), color='black', linestyle='-', linewidth=2, label='Task deadline')

# Draw a vertical dashed line at the start time
plt.axvline(x=start_time, color='black', linestyle='-', linewidth=1)
# Draw a vertical dashed line at the end time
plt.axvline(x=end_time, color='black', linestyle='-', linewidth=1)
upper_patch = Patch(facecolor='none', edgecolor='black', hatch='//', label='Tasks are interrupted')
lower_patch = Patch(facecolor='none', edgecolor='black', hatch='..', label='Tasks are running')


# plt.axhline(y=lower_threshold, color='red', linestyle='--', linewidth=1)

# Annotate the threshold line
plt.annotate(f'Task is submitted here',
             xy=(submitted_time, 250),
             xytext=(pd.Timestamp("2022-10-01 14:00"), 250 + 100),
             arrowprops=dict(arrowstyle='->',color='black'),
             fontsize=my_fontsize,
             color='black')

plt.annotate(f'Task is delayed until here',
             xy=(start_time, 150),
             xytext=(pd.Timestamp("2022-10-01 14:00"), 200),
             arrowprops=dict(arrowstyle='->',color='black'),
             fontsize=my_fontsize,
             color='black')


plt.title('Carbon Intensity in the first two days of October 2022', fontsize=my_fontsize)
plt.xlabel('Days and Hours', fontsize=my_fontsize)
plt.ylabel('Carbon Intensity (gCO2/kWh)', fontsize=my_fontsize)
plt.grid(True)

handles, labels = plt.gca().get_legend_handles_labels()

# Add legend
handles.append(upper_patch)
labels.append('Tasks are interrupted')

handles.append(lower_patch)
labels.append('Greenest Window')

plt.legend(handles=handles, labels=labels, fontsize=my_fontsize)

plt.tight_layout()
plt.savefig("waitawhile_2_visualization.pdf")

