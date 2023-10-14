import pandas as pd
import os

merged_data = pd.DataFrame()

# Iterate over CSV files in the directory
for filename in os.listdir("results/attention"):
    if filename.endswith(".csv"):
        file_path = os.path.join("results/attention", filename)

        # Read the CSV file
        data = pd.read_csv(file_path)

        # Merge the data based on the specified columns
        columns_to_merge = ["Participant_ID", "Age", "Sports_Experience", "Reaction_Time", "Color"]
        merged_data = pd.concat([merged_data, data[columns_to_merge]])

# Save the merged data to a new CSV file
merged_data.to_csv("merged_results.csv", index=False)