import matplotlib.pyplot as plt
import matplotlib
FIG_NAME = "carbon_emission_0error_in_percentage_SE.pdf"

error = "0"
forecast_error = f"{error}-error-forecast"
current_country_in_text = "Sweden"
carbon_filename = "carbon_traces/SE_2022_hourly.parquet"
matplotlib.rc('xtick', labelsize=24) 
matplotlib.rc('ytick', labelsize=24)

categories = ['ST[40]' ,'ST[40]\nwith TaskStopper', 'DT[40,60]', 'Greenest\nWindow', 'WaitAWhile']
carbon_emission_removal = [279.72, 279.045, 278.607, 277.048, 274.90]
width = 10
x1 = 10
x2 = 30
x3 = 50
x4 = 70
x5 = 90

FCFS = 282.33
carbon_percentage_removal = []

for carbon_removal in carbon_emission_removal:
    
    percentage_removal = (1 - (carbon_removal/FCFS)) * 100
    carbon_percentage_removal.append(percentage_removal)

plt.figure(figsize=(12,10))
plt.bar(x1, carbon_percentage_removal[0], width, label='Without Interruption', facecolor="darksalmon", edgecolor="black", hatch="//")
plt.bar(x2, carbon_percentage_removal[1], width, label='With Interruption', facecolor="steelblue", edgecolor="black", hatch="\\")
plt.bar(x3, carbon_percentage_removal[2], width, facecolor="steelblue", edgecolor="black", hatch=".")
plt.bar(x4, carbon_percentage_removal[3], width, facecolor="darksalmon", edgecolor="black", hatch="o")
plt.bar(x5, carbon_percentage_removal[4], width, facecolor="steelblue", edgecolor="black")

plt.xticks([10,30,50,70,90], categories)

# plt.legend()
plt.ylabel('Carbon Reduction (%)', fontsize=30)
plt.title(f'Carbon Reduction in {current_country_in_text}', fontsize=30)
plt.xlabel("Schedulers", fontsize=30)
plt.grid(True, linestyle="--", axis="y")
plt.legend(fontsize=30)
# Save the chart as an image
plt.tight_layout()
plt.savefig(FIG_NAME)  # Saves as PNG in the current directory