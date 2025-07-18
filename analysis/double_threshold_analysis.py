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

matplotlib.rc('xtick', labelsize=22) 
matplotlib.rc('ytick', labelsize=24) 

# Filenames
FCFS_host_filename = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/host.parquet"
FCFS_power_filename = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
FCFS_service_filename = f"output/{forecast_error}/surfsara_month/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_10_20_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_20/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_10_20_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_20/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_10_20_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_20/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_10_40_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_40/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_10_40_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_40/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_10_40_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_40/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_10_60_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_60/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_10_60_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_60/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_10_60_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_10_60/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_20_40_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_20_40/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_20_40_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_20_40/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_20_40_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_20_40/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_20_60_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_20_60/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_20_60_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_20_60/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_20_60_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_20_60/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_30_40_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_30_40/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_30_40_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_30_40/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_30_40_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_30_40/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_30_60_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_30_60/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_30_60_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_30_60/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_30_60_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_30_60/raw-output/{current_country_in_number}/seed=0/service.parquet"

DT_40_60_host_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_40_60/raw-output/{current_country_in_number}/seed=0/host.parquet"
DT_40_60_power_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_40_60/raw-output/{current_country_in_number}/seed=0/powerSource.parquet"
DT_40_60_service_filename = f"output/{forecast_error}/surfsara_month_doublethreshold_40_60/raw-output/{current_country_in_number}/seed=0/service.parquet"

# Labels
scheduler_labels = ['[10,20]', '[10,40]', '[10,60]',
                    '[20,40]', '[20,60]',
                    '[30,40]', '[30,60]',
                    '[40,60]']

# Data containers
carbon_emission_values = []
carbon_emission_in_percentage = []
cpu_idle_time_values = []
power_draw_values = []
embodied_carbon_values = []
makespan_values = []

# Mapping of scheduler variants
list_of_schedulers = {
    DT_10_20_host_filename: DT_10_20_power_filename, DT_10_40_host_filename: DT_10_40_power_filename,
    DT_10_60_host_filename: DT_10_60_power_filename,
    DT_20_40_host_filename: DT_20_40_power_filename, DT_20_60_host_filename: DT_20_60_power_filename,
    DT_30_40_host_filename: DT_30_40_power_filename, DT_30_60_host_filename: DT_30_60_power_filename,
    DT_40_60_host_filename: DT_40_60_power_filename
}

list_of_services = [
    DT_10_20_service_filename, DT_10_40_service_filename,
    DT_10_60_service_filename,
    DT_20_40_service_filename, DT_20_60_service_filename,
    DT_30_40_service_filename, DT_30_60_service_filename,
    DT_40_60_service_filename
]

carbon_file = pd.read_parquet(carbon_filename, engine="pyarrow")
# Data extraction
for (host_filename, power_filename) in list_of_schedulers.items():
    powerSource = pd.read_parquet(power_filename, engine="pyarrow")
    carbon_emission = powerSource["carbon_emission"].sum() / 1000.0
    host = pd.read_parquet(host_filename, engine="pyarrow")
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

powerSource = pd.read_parquet(FCFS_power_filename,engine="pyarrow")
baseline_carbon_emission = powerSource["carbon_emission"].sum() / 1000.0
for value in carbon_emission_values:
    percent = (1 - value/baseline_carbon_emission) * 100.0
    carbon_emission_in_percentage.append(percent)
    

plt.figure(figsize=(12, 10))
plt.plot(scheduler_labels, carbon_emission_in_percentage, linestyle="-", marker='o', color='steelblue', label=current_country_in_text)

plt.xlabel('Double-Threshold variants', fontsize=30)
plt.ylabel('Carbon Reduction (%)', fontsize=30)
plt.title(f'Carbon Reduction in {current_country_in_text}', fontsize=30)
plt.legend(fontsize=24)

# Show the plot
plt.grid(True)
plt.savefig(f'double_threshold_carbon_emission_{error}error_{current_country_in_text}.pdf', bbox_inches='tight')