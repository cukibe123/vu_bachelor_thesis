import matplotlib.pyplot as plt
import matplotlib
FIG_NAME = "carbon_emission_0error_in_percentage_BE.pdf"

error = "0"
forecast_error = f"{error}-error-forecast"
current_country_in_text = "Belgium"
carbon_filename = "carbon_traces/BE_2022_hourly.parquet"
matplotlib.rc('xtick', labelsize=24) 
matplotlib.rc('ytick', labelsize=24)

categories = ['ST[30]' ,'ST[35]\nwith TaskStopper', 'DT[40,60]', 'Greenest\nWindow', 'WaitAWhile']
carbon_emission_removal = [2569.5324, 2534.500, 2533.74, 2530.724, 2460.848]
width = 10
x1 = 10
x2 = 30
x3 = 50
x4 = 70
x5 = 90

FCFS = 2629.216
carbon_percentage_removal = []

for carbon_removal in carbon_emission_removal:
    
    percentage_removal = (1 - (carbon_removal/FCFS)) * 100
    carbon_percentage_removal.append(percentage_removal)

plt.figure(figsize=(12,10))
plt.bar(x1, carbon_percentage_removal[0], width, label='ST[30]-noTaskStopper', facecolor="darksalmon", edgecolor="black", hatch="//")
plt.bar(x2, carbon_percentage_removal[1], width, label='ST[40]', facecolor="coral", edgecolor="black", hatch="\\")
plt.bar(x3, carbon_percentage_removal[2], width, label='DT[30,40]', facecolor="steelblue", edgecolor="black", hatch=".")
plt.bar(x4, carbon_percentage_removal[3], width, label='Greenest-Window', facecolor="lightblue", edgecolor="black", hatch="o")
plt.bar(x5, carbon_percentage_removal[4], width, label='WaitAWhile', facecolor="mediumseagreen", edgecolor="black")

plt.xticks([10,30,50,70,90], categories)

# plt.legend()
plt.ylabel('Carbon Reduction (%)', fontsize=30)
plt.title(f'Carbon Reduction in {current_country_in_text}', fontsize=30)
plt.xlabel("Schedulers", fontsize=30)
plt.grid(True, linestyle="--", axis="y")
# Save the chart as an image
plt.tight_layout()
plt.savefig(FIG_NAME)  # Saves as PNG in the current directory