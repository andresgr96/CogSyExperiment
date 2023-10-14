import pandas as pd
import os

def merge_csv(memory_merged_data, attention_merged_data):
   

    # Iterate attention CSV files in the directory
    for filename in os.listdir("results/attention"):
        if filename.endswith(".csv"):
            file_path = os.path.join("results/attention", filename)

            # Read the CSV file
            data = pd.read_csv(file_path)

            # Merge the data based on the specified columns
            columns_to_merge = ["Participant_ID", "Age", "Sports_Experience", "Reaction_Time", "Color"]
            memory_merged_data = pd.concat([memory_merged_data, data[columns_to_merge]])

    # Save the merged data to a new CSV file
    memory_merged_data.to_csv("attention_merged_results.csv", index=False)

    for filename in os.listdir("results/memory"):
        if filename.endswith(".csv"):
            file_path = os.path.join("results/memory", filename)

            # Read the CSV file
            data = pd.read_csv(file_path)

            # Merge the data based on the specified columns
            columns_to_merge = ["Participant_ID", "Age", "Sports_Experience", "Correct", "Number_Shown", "Color"]
            attention_merged_data = pd.concat([attention_merged_data, data[columns_to_merge]])

    # Save the merged data to a new CSV file
    attention_merged_data.to_csv("memory_merged_results.csv", index=False)

    return memory_merged_data, attention_merged_data
