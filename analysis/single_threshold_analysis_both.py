import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib
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
error = "0"
forecast_error = f"{error}-error-forecast"
current_country_in_number = CA
current_country_in_text = "Canada"
carbon_filename = "carbon_traces/CA_2022_hourly.parquet"
my_fontsize = 24

matplotlib.rc('xtick', labelsize=my_fontsize) 
matplotlib.rc('ytick', labelsize=my_fontsize)

# Filenames
FCFS_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/host.parquet"
FCFS_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
FCFS_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_10_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_10/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_10_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_10/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_10_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_10/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_15_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_15/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_15_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_15/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_15_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_15/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_20_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_20/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_20_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_20/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_20_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_20/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_25_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_25/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_25_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_25/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_25_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_25/raw-output/{current_country_in_number}0/seed=0/service.parquet"

ST_30_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_30/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_30_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_30/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_30_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_30/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_35_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_35/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_35_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_35/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_35_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_35/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_40_host_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_40/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_40_power_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_40/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_40_service_filename_notaskstop = f"output/{forecast_error}/surfsara_month_singlethreshold_no_taskstop_40/raw-output/{current_country_in_number}/seed=0/service.parquet"

FCFS_host_filename = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/host.parquet"
FCFS_power_filename = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
FCFS_service_filename = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_10_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_10/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_10_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_10/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_10_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_10/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_15_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_15/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_15_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_15/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_15_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_15/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_20_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_20/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_20_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_20/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_20_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_20/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_25_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_25/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_25_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_25/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_25_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_25/raw-output/{current_country_in_number}0/seed=0/service.parquet"

ST_30_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_30/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_30_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_30/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_30_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_30/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_35_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_35/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_35_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_35/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_35_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_35/raw-output/{current_country_in_number}/seed=0/service.parquet"

ST_40_host_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_40/raw-output/{current_country_in_number}/seed=0/host.parquet"
ST_40_power_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_40/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
ST_40_service_filename = f"output/{forecast_error}/surfsara_month_singlethreshold_40/raw-output/{current_country_in_number}/seed=0/service.parquet"

# Labels
scheduler_labels = ['ST[10]', 'ST[15]', 'ST[20]', 'ST[25]', 'ST[30]', 'ST[35]', 'ST[40]']

# Data containers
carbon_emission_values_notaskstop = []
carbon_emission_in_percentage_notaskstop = []

carbon_emission_values = []
carbon_emission_in_percentage = []

# Mapping of scheduler variants
list_of_schedulers = {
    ST_10_host_filename: ST_10_power_filename,
    ST_15_host_filename: ST_15_power_filename,  
    ST_20_host_filename: ST_20_power_filename,
    ST_25_host_filename: ST_25_power_filename,
    ST_30_host_filename: ST_30_power_filename,
    ST_35_host_filename: ST_40_power_filename,
    ST_40_host_filename: ST_40_power_filename
}

list_of_services = [ST_10_service_filename, ST_15_service_filename, ST_20_service_filename,
                    ST_25_service_filename, ST_30_service_filename, ST_35_service_filename, ST_40_service_filename]

# Mapping of scheduler variants
list_of_schedulers_notaskstop = {
    ST_10_host_filename_notaskstop: ST_10_power_filename_notaskstop,
    ST_15_host_filename_notaskstop: ST_15_power_filename_notaskstop,  
    ST_20_host_filename_notaskstop: ST_20_power_filename_notaskstop,
    ST_25_host_filename_notaskstop: ST_25_power_filename_notaskstop,
    ST_30_host_filename_notaskstop: ST_30_power_filename_notaskstop,
    ST_35_host_filename_notaskstop: ST_40_power_filename_notaskstop,
    ST_40_host_filename_notaskstop: ST_40_power_filename_notaskstop
}

list_of_services_notaskstop = [ST_10_service_filename_notaskstop, ST_15_service_filename_notaskstop, ST_20_service_filename_notaskstop,
                            ST_25_service_filename_notaskstop, ST_30_service_filename_notaskstop, ST_35_service_filename_notaskstop, 
                            ST_40_service_filename_notaskstop]

carbon_file = pd.read_parquet(carbon_filename, engine="pyarrow")

def extract_carbon_emission(list_of_schedulers, carbon_emission_values):
    for (host_filename, power_filename) in list_of_schedulers.items():
        host = pd.read_parquet(host_filename, engine="pyarrow")
        powerSource = pd.read_parquet(power_filename, engine="pyarrow")

        carbon_emission = powerSource["carbon_emission"].sum() / 1000.0
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
        carbon_emission_values.append(carbon_emission)
    
extract_carbon_emission(list_of_schedulers, carbon_emission_values)
extract_carbon_emission(list_of_schedulers_notaskstop, carbon_emission_values_notaskstop)

powerSource = pd.read_parquet(FCFS_power_filename,engine="pyarrow")
baseline_carbon_emission = powerSource["carbon_emission"].sum() / 1000.0
for value in carbon_emission_values:
    percent = (1 - value/baseline_carbon_emission) * 100.0
    carbon_emission_in_percentage.append(percent)
    
for value in carbon_emission_values_notaskstop:
    percent = (1 - value/baseline_carbon_emission) * 100.0
    carbon_emission_in_percentage_notaskstop.append(percent)

plt.figure(figsize=(12, 10))
plt.plot(scheduler_labels, carbon_emission_in_percentage, linestyle="-", marker='o', color='coral', label=f"{current_country_in_text} with TaskStopper")
plt.plot(scheduler_labels, carbon_emission_in_percentage_notaskstop, linestyle="--", marker='*', color='darksalmon', label=f"{current_country_in_text}")

plt.xlabel('Single-Threshold',fontsize=30)
plt.ylabel('Carbon Reduction (%)',fontsize=30)
plt.title(f'Carbon Reduction in {current_country_in_text}',fontsize=30)
plt.legend(fontsize=my_fontsize)

# Show the plot
plt.grid(True)
plt.savefig(f'single_threshold_carbon_emission_{error}error_{current_country_in_text}_both.pdf')