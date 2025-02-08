
from ConnectToGarmin import fetch_data
from JsonToCsvConversionCleaup import convert_to_csv
from GraphAnalysis import plot_graph

# Step 1: Fetch data from Garmin API
data = fetch_data()

# Step 2: Convert the data to CSV
csv_file = "heart_rate_data.csv"
convert_to_csv(data, csv_file)

# Step 3: Plot the graph
plot_graph(csv_file)
