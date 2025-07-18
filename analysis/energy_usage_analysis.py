import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib
# Filenames
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
ST = "surfsara_month_singlethreshold_35"
DT = "surfsara_month_doublethreshold_30_40"
waitawhile_2 = "surfsara_month_waitawhile_2"
waitawhile_3 = "surfsara_month_waitawhile_3"
FCFS  = "surfsara_month"
COUNTRY = "Netherlands"
COUNTRY_SHORT = "NL"
IDLE_ENERGY_USAGE = 32140.8 #kW/hour

my_fontsize=22
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)

plt.figure(figsize=(20, 6))

filename_list = [ST, waitawhile_3, FCFS]
label_list = ["ST[40]", "WaitAWhile", "FCFS"]

for filename, label in zip(filename_list, label_list):
    power_filename = f"output/{carbon_error}/{filename}/raw-output/{country_in_numbers}/seed=0/powerSource.parquet"
    power = pd.read_parquet(power_filename, engine="pyarrow")
    
    
    power['timestamp_absolute'] = pd.to_datetime(power['timestamp_absolute'], unit='ms')
    power.set_index('timestamp_absolute', inplace=True)
    power = power['2022-10-01':'2022-10-15']
    power["energy_usage"] = power["energy_usage"] / 1000
    power["energy_usage_without_idle"] = power["energy_usage"] - IDLE_ENERGY_USAGE
    total_energy_usage = power['energy_usage'].sum()
    
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
    else:
        linestyle = '-'
        color = 'green'

    energy_usage_without_idle_power = power['energy_usage_without_idle'].sum()
    based_idle_energy_usage = total_energy_usage - energy_usage_without_idle_power

    plt.plot(power.index, power["energy_usage"], label=label, linestyle=linestyle, linewidth=1, color=color)

plt.axhline(y=IDLE_ENERGY_USAGE, color='black', linestyle='-', linewidth=1, label="Baseline energy usage")
plt.axhspan(ymin=0,ymax=IDLE_ENERGY_USAGE, facecolor="none", hatch="//",alpha=0.5, label="Not shiftable")

print(f"Total energy usage is {total_energy_usage}")
print(f"Total energy usage without idle power is {energy_usage_without_idle_power}")
print(f"Total based energy usage is {based_idle_energy_usage}")

plt.xlabel("Date", fontsize = 30)
plt.ylabel("Energy usage (kWh)", fontsize = 30)
plt.title(f"Energy Usage over October 2022 - Netherlands", fontsize = 30)
plt.legend(fontsize = 24)
plt.tight_layout()
plt.savefig(f"energy-usage-{COUNTRY}.pdf")
plt.close() 