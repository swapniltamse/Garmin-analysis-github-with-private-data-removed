
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ast  # To parse string representations of lists

# Load the data
df = pd.read_csv("garmin_heart_rate.csv", parse_dates=["timestamp"])

# Convert heartRateValues from string to list
df["heartRateValues"] = df["heartRateValues"].apply(ast.literal_eval)

# Flatten the heart rate values into a new DataFrame
heart_rate_records = []
for _, row in df.iterrows():
    for timestamp, hr in row["heartRateValues"]:
        heart_rate_records.append({"timestamp": pd.to_datetime(timestamp, unit="ms"), "heart_rate": hr})

# Create a new DataFrame
hr_df = pd.DataFrame(heart_rate_records)

threshold = df["abnormalHrThresholdValue"].max()  # Get the threshold
abnormal_hr = hr_df[hr_df["heart_rate"] > threshold]  # Filter out abnormal values

# Plot with abnormalities highlighted
plt.figure(figsize=(12, 6))
plt.plot(hr_df["timestamp"], hr_df["heart_rate"], label="Heart Rate", color="blue")
plt.scatter(abnormal_hr["timestamp"], abnormal_hr["heart_rate"], color="red", label="Abnormal HR", marker="o")
plt.axhline(y=threshold, color="r", linestyle="--", label=f"Threshold: {threshold} bpm")

# ** Format x-axis to show hours only **
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d %H:%M"))  # Show HH:MM format
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=12))  # Show every hour

# Rotate and format the x-axis labels for better readability
plt.xticks(rotation=45, ha="center")  # Center-align labels below the axis

# Set x-axis labels below the axis
plt.gca().tick_params(axis='x', labelbottom=True)

plt.xlabel("Time")
plt.ylabel("Heart Rate (bpm)")
plt.title("Heart Rate with Abnormalities Highlighted")
plt.legend()
plt.show()