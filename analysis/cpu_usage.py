import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib

# Filenames
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
country_in_numbers = NL

my_fontsize=22
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)


filename_list = [ST_no_taskstop, DT, waitawhile_2, FCFS]
label_list = ["ST[20]", "DT[30,60]", "Greenest-Window", "FCFS"]

plt.figure(figsize=(20, 8))

for filename,label in zip(filename_list,label_list):
    host_filename = f"output/{carbon_error}/{filename}/raw-output/{country_in_numbers}/seed=0/host.parquet"
    host = pd.read_parquet(host_filename, engine="pyarrow")
    usage_over_time = host.groupby('timestamp')['cpu_usage'].sum().reset_index()
    usage_over_time["cpu_usage"] = usage_over_time["cpu_usage"].rolling(window=3, min_periods=1).mean()
    if (filename == ST):
        plt.plot(usage_over_time["timestamp"]/3_600_000 / 24, usage_over_time["cpu_usage"], label=label, linestyle='--', linewidth=1, color="coral")
    elif (filename == DT):
        plt.plot(usage_over_time["timestamp"]/3_600_000 / 24, usage_over_time["cpu_usage"], label=label, linestyle=':', linewidth=1, color="steelblue")
    elif (filename == waitawhile_2):
        plt.plot(usage_over_time["timestamp"]/3_600_000 / 24, usage_over_time["cpu_usage"], label=label, linestyle='-.', linewidth=1, color="blue")
    elif (filename == waitawhile_3):
        plt.plot(usage_over_time["timestamp"]/3_600_000 / 24, usage_over_time["cpu_usage"], label=label, linestyle='--', linewidth=1, color="mediumseagreen")
    elif (filename == ST_no_taskstop):
        plt.plot(usage_over_time["timestamp"]/3_600_000 / 24, usage_over_time["cpu_usage"], label=label, linestyle='--', linewidth=1, color="darksalmon")
    else:
        plt.plot(usage_over_time["timestamp"]/3_600_000 / 24, usage_over_time["cpu_usage"], label=label, linestyle='-', linewidth=1, color="green")
    
plt.xlabel("Time [days]",fontsize=30)
plt.ylabel("The amount of CPU usage (MHz)",fontsize=30)
plt.title(f"The amount of CPU Usage over October 2022 - {COUNTRY}",fontsize=30)
plt.legend(fontsize=30)
plt.tight_layout()
plt.savefig(f"cpu_usage_{COUNTRY_SHORT}.pdf")
plt.close()

