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
my_fontsize=14
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)



plt.figure(figsize=(12, 6))
plt.plot(NL_October_2022.index, NL_October_2022['carbon_intensity'], label='Netherlands', linestyle='-',linewidth="2")



original_start_time = pd.Timestamp("2022-10-01 0:00")
original_end_time = pd.Timestamp("2022-10-02 23:00")

submitted_time = pd.Timestamp("2022-10-01 0:00")
y_start_1 = 300

y_start_2 = 130

width = pd.Timedelta(hours=8)
height = 20

rect = patches.Rectangle((submitted_time, y_start_1), width, height,
                         linewidth=2, facecolor='none', edgecolor='black', alpha=1,
                         label='Submitted Task')
plt.gca().add_patch(rect)

start_time = pd.Timestamp("2022-10-01 0:00")
end_time = pd.Timestamp("2022-10-01 6:00")

start_chunk_1 = pd.Timestamp("2022-10-01 0:00")
width_chunk_1 = pd.Timedelta(hours=2)
end_chunk_1 = pd.Timestamp("2022-10-01 2:00")

start_chunk_2 = pd.Timestamp("2022-10-01 8:00")
width_chunk_2 = pd.Timedelta(hours=6)
end_chunk_2 = pd.Timestamp("2022-10-01 14:00")

chunk_1 = patches.Rectangle((start_chunk_1, 150), width_chunk_1, height,
                         linewidth=1, color='black', alpha=0.5,
                         label='First Chunk')

plt.gca().add_patch(chunk_1)

# rect_2 = patches.Rectangle((start_time, y_start_2), width, height,
#                          linewidth=1, color='red', alpha=0.5,
#                          )
# plt.gca().add_patch(rect_2)

plt.axvspan(start_chunk_1, end_chunk_1,
            facecolor='none', hatch='/', alpha=1)

plt.axvspan(start_chunk_2, end_chunk_2,
            facecolor='none', hatch='/', alpha=1)

# Draw a vertical dashed line at the start time
plt.axvline(x=start_chunk_1, color='black', linestyle='--', linewidth=1)
# Draw a vertical dashed line at the end time
plt.axvline(x=end_chunk_1, color='black', linestyle='--', linewidth=1)

plt.axvline(x=start_chunk_2, color='black', linestyle='--', linewidth=1)
# Draw a vertical dashed line at the end time
plt.axvline(x=end_chunk_2, color='black', linestyle='--', linewidth=1)

plt.axvline(x=pd.Timestamp("2022-10-02 00:00"), color='black', linestyle='-', linewidth=2,label='Task deadline')

upper_patch = Patch(facecolor='none', edgecolor='black', hatch='//')

# Annotate the threshold line
plt.annotate(f'Task is submitted here',
             xy=(submitted_time, y_start_1 + 20),
             xytext=(original_start_time, y_start_1 + 50),
             arrowprops=dict(arrowstyle='->',color='black'),
             fontsize=my_fontsize,
             color='black')

plt.annotate(f'Low carbon slots',
             xy=(pd.Timestamp("2022-10-01 1:00"), 375),
             xytext=(pd.Timestamp("2022-10-01 2:15"), 400),
             arrowprops=dict(arrowstyle='-',color='black', alpha=1),
             fontsize=my_fontsize,
             color='black')

plt.annotate(text='',
             xy=(pd.Timestamp("2022-10-01 11:00"), 375),
             xytext=(pd.Timestamp("2022-10-01 6:00"), 395),
             arrowprops=dict(arrowstyle='-',color='black', alpha=1),
             fontsize=my_fontsize,
             color='black')


# First chunk vertical lines
plt.plot([submitted_time, start_chunk_1], [300, 170],
         linestyle='--', color='black', alpha=1)

plt.plot([end_chunk_1, end_chunk_1], [300, 170],
         linestyle='--', color='black', alpha=1)


chunk_2 = patches.Rectangle((start_chunk_2, 130), width_chunk_2, height,
                         linewidth=1, color='black', alpha=0.5,
                         label='Second Chunk')

plt.gca().add_patch(chunk_2)

# Second chunk vertical lines
plt.plot([pd.Timestamp("2022-10-01 2:00"), start_chunk_2], [300, 150],
         linestyle='--', color='black', alpha=1)

plt.plot([pd.Timestamp("2022-10-01 8:00"), end_chunk_2], [300, 150],
         linestyle='--', color='black', alpha=1)

handles, labels = plt.gca().get_legend_handles_labels()

# Add legend
handles.append(upper_patch)
labels.append('Selected Time Slots')

plt.legend(handles=handles, labels=labels, fontsize=my_fontsize)
plt.ylim(bottom=min(0, plt.ylim()[0]), top=plt.ylim()[1])   

plt.title('Carbon Intensity in the first two days of October 2022', fontsize=18)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Carbon Intensity (gCO2/kWh)', fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.savefig("waitawhile_3_visualization.png")

