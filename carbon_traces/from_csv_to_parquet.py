import pandas as pd
import pyarrow as pa
import numpy as np

filename = "AT_2022_hourly"

df = pd.read_csv(f'{filename}.csv')

columns_to_keep = ['timestamp', 'carbon_intensity']
df_filtered = df[columns_to_keep]

# Save to Parquet
df_filtered.to_parquet('FR_2022_hourly.parquet', engine='pyarrow')

df = pd.read_parquet('FR_2022_hourly.parquet', engine='pyarrow')

df["timestamp"] = pd.to_datetime(df["timestamp"], yearfirst=True, utc=True)

df["timestamp"] = df["timestamp"].astype("int64") // 10**6

df.to_parquet("FR_2022_hourly.parquet", index=False)

df_filtered["timestamp"] = pd.to_datetime(df_filtered["timestamp"], yearfirst=True, utc=True)

df_filtered["timestamp"] = df_filtered["timestamp"].astype('int64') // 10**6  # Convert ns to ms

# Save back to Parquet
df_filtered.to_parquet(f"{filename}.parquet", engine='pyarrow')