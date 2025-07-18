import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib
# Filenames
carbon_error = "0-error-forecast"
error_array = ["0","5","10","15","20"]
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
current_country_in_number = CA
current_country_in_text = "Canada"
carbon_file_name = "carbon_traces/CA_2022_hourly.parquet"
carbon_file = pd.read_parquet(carbon_file_name, engine="pyarrow")
FIGNAME = f"error_forecast_{current_country_in_text}.pdf"
my_fontsize=24
matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)

ST_no_taskstop = "surfsara_month_singlethreshold_no_taskstop_35"
ST = "surfsara_month_singlethreshold_35"
DT = "surfsara_month_doublethreshold_40_60"
waitawhile_2 = "surfsara_month_waitawhile_2"
waitawhile_3 = "surfsara_month_waitawhile_3"
labels = ["ST[35]", "ST[35] with TaskStopper", "DT[40,60]", "Greenest-Window", "WaitAWhile"]

ST_no_taskstop_value = []
ST_no_taskstop_percentage = []
ST_value = []
ST_percentage = []
DT_value = []
DT_percentage = []
waitawhile_2_value = []
waitawhile_2_percentage = []
waitawhile_3_value = []
waitawhile_3_percentage = []



def extract_carbon_emission(scheduler_name, value_array):
    for error in error_array:
        host_filename = f"output/{error}-error-forecast/{scheduler_name}/raw-output/{current_country_in_number}/seed=0/host.parquet"
        power_filename = f"output/{error}-error-forecast/{scheduler_name}/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
        
        host = pd.read_parquet(host_filename, engine="pyarrow")
        power = pd.read_parquet(power_filename, engine="pyarrow")
        
        carbon_emission = power["carbon_emission"].sum() / 1000.0
        host_after = host[host["timestamp_absolute"] >= 1667170800000]
        host_after = host_after[host_after["cpu_usage"] == 0]

        idle_carbon_emission = 0
        power_draw_idle_const = 0.032

        for index, row in host_after.iterrows():
            target_timestamp = row['timestamp_absolute']
            power_draw_idle = row['power_draw']
            result = carbon_file[carbon_file["timestamp"] == target_timestamp]
            if (power_draw_idle == 32):
                if not result.empty:
                    carbon_intensity = result.iloc[0]["carbon_intensity"]
                    # print("Carbon Intensity:", carbon_intensity)
                    carbon_out = power_draw_idle_const * carbon_intensity / 1000.0
                    idle_carbon_emission = idle_carbon_emission + carbon_out
                else:
                    timestamp_diff = (carbon_file["timestamp"] - target_timestamp).abs()
                    closest_row = carbon_file.loc[timestamp_diff.idxmin()]
                    carbon_intensity = closest_row["carbon_intensity"]
                    carbon_out = power_draw_idle_const * carbon_intensity / 1000.0
                    idle_carbon_emission = idle_carbon_emission + carbon_out
        
        carbon_emission = carbon_emission - idle_carbon_emission
        value_array.append(carbon_emission)
        
        
FCFS_power_filename = f"output/0-error-forecast/surfsara_month/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
powerSource = pd.read_parquet(FCFS_power_filename,engine="pyarrow")
baseline_carbon_emission = powerSource["carbon_emission"].sum() / 1000.0

def calculate_saving_percentage(carbon_value_array, carbon_percentage_array):
    for value in carbon_value_array:
        percent = (1 - value/baseline_carbon_emission) * 100.0
        carbon_percentage_array.append(percent)
        
extract_carbon_emission(ST_no_taskstop, ST_no_taskstop_value)
extract_carbon_emission(ST, ST_value)
extract_carbon_emission(DT, DT_value)
extract_carbon_emission(waitawhile_2, waitawhile_2_value)
extract_carbon_emission(waitawhile_3, waitawhile_3_value)

calculate_saving_percentage(ST_value, ST_percentage)
calculate_saving_percentage(ST_no_taskstop_value, ST_no_taskstop_percentage)
calculate_saving_percentage(DT_value, DT_percentage)
calculate_saving_percentage(waitawhile_2_value, waitawhile_2_percentage)
calculate_saving_percentage(waitawhile_3_value, waitawhile_3_percentage)

plt.figure(figsize=(12,8))
plt.plot(error_array, ST_no_taskstop_percentage, color="darksalmon", linestyle="--", linewidth=1, label=labels[0])
plt.plot(error_array, ST_percentage, color="coral", linestyle="-", marker='o', linewidth=1, label=labels[1])
plt.plot(error_array, DT_percentage, color="steelblue", linestyle="-",linewidth=1, label=labels[2])
plt.plot(error_array, waitawhile_2_percentage, color="blue", linestyle=":", linewidth=3, label=labels[3])
plt.plot(error_array, waitawhile_3_percentage, color="mediumseagreen", linestyle="-.", linewidth=1, label=labels[4])
plt.ylim(bottom=min(0, plt.ylim()[0]), top=plt.ylim()[1])

plt.legend(fontsize=23, framealpha=0.3)
plt.ylabel("Carbon Reduction (%)", fontsize=30)
plt.xlabel("Carbon Forecast Error (%)", fontsize=30)
plt.title(current_country_in_text,fontsize=30)
plt.grid(True)
plt.savefig(FIGNAME)