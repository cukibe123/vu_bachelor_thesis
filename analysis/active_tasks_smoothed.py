import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib
# Filenames
ST_no_taskstop = "surfsara_month_singlethreshold_no_taskstop_20"
ST = "surfsara_month_singlethreshold_40"
DT = "surfsara_month_doublethreshold_30_60"
waitawhile_2 = "surfsara_month_waitawhile_2"
waitawhile_3 = "surfsara_month_waitawhile_3"
FCFS  = "surfsara_month"
COUNTRY = "Netherlands"
COUNTRY_SHORT = "NL"
carbon_error = "0-error-forecast"
NL = "0"
BE = "1"
DE = "2"
FR = "3"
VN = "4"
US = "5"
AU = "6"
AT = "7"
SE = "8"
CA = "9"
country_in_numbers = NL

my_fontsize=22
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)
filename_list = [ST_no_taskstop, DT, waitawhile_2, FCFS]
label_list = ["ST[20]", "DT[30,60]", "Greenest-Window", "FCFS"]

plt.figure(figsize=(20, 6))

for filename, label in zip(filename_list, label_list):
    service_filename = f"output/{carbon_error}/{filename}/raw-output/{country_in_numbers}/seed=0/service.parquet"
    service = pd.read_parquet(service_filename, engine="pyarrow")
    
    # Convert timestamp to days
    service['timestamp_absolute'] = pd.to_datetime(service['timestamp_absolute'], unit='ms')
    service.set_index('timestamp_absolute', inplace=True)
    service = service['2022-10-01':'2022-10-15']
    
    # Compute rolling average (window=6)
    service["tasks_active_smooth"] = service["tasks_active"].rolling(window=1, min_periods=1).mean()
    
    # Choose linestyle
    if filename == ST:
        linestyle = '--'
        color = "coral"
    elif filename == DT:
        linestyle = ':'
        color = 'steelblue'
    elif filename == waitawhile_2:
        linestyle = '-.'
        color = 'lightblue'
    elif filename == waitawhile_3:
        linestyle = '--'  # Marker removed to keep it clean
        color = 'mediumseagreen'
    elif filename == ST_no_taskstop:
        linestyle = '--'
        color = 'darksalmon'
    else:
        linestyle = '-'
        color = 'green'
    
    # Plot smoothed data
    plt.plot(service.index, service["tasks_active_smooth"], label=label, linestyle=linestyle, linewidth=1, color=color)

plt.xlabel("Date",fontsize=30)
plt.ylabel("Number of active tasks",fontsize=30)
plt.title(f"Active Tasks over October 2022 - {COUNTRY}",fontsize=30)
plt.legend(fontsize=my_fontsize, framealpha=0.1)
plt.tight_layout()
plt.grid(True)
plt.savefig(f"active-tasks-smoothed-{COUNTRY_SHORT}.pdf")
plt.close()