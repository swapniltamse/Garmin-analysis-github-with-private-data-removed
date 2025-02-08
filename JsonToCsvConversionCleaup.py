# csv_conversion.py

import pandas as pd
import json

# Function to convert JSON data to CSV
def convert_to_csv(json_data, output_file):
    """
    Convert Garmin heart rate JSON data to CSV format.

    Parameters:
        json_data (dict): The Garmin JSON data.
        output_file (str): The path where the CSV file should be saved.
    """
with open("garmin_heart_rate.json", "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Expand heart rate readings
if "heart_rate" in df.columns:
    df = df.join(pd.json_normalize(df["heart_rate"])).drop(columns=["heart_rate"])

# Print available columns for debugging
print("Columns available:", df.columns)

# Convert 'startTimestampGMT' to datetime format
df["timestamp"] = pd.to_datetime(df["startTimestampGMT"])

# Set timestamp as index
df.set_index("timestamp", inplace=True)

# Export DataFrame to CSV
df.to_csv("garmin_heart_rate.csv")
