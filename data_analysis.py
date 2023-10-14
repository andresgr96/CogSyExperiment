import matplotlib.pyplot as plt
import ast
from merge_csv import merge_csv
import pandas as pd

memory_merged_data = pd.DataFrame()
attention_merged_data = pd.DataFrame()

# Will update the CSV everytime we add another experiment data 
attention, memory = merge_csv(memory_merged_data, attention_merged_data)

def plot_reaction_time_vs_color(data, output_filename):
    # Convert the Color column from string to tuple
    data['Color'] = data['Color'].apply(lambda x: ast.literal_eval(x))

    # Extract Reaction Time and Color columns
    reaction_time = data['Reaction_Time']
    colors = data['Color']

    # Convert RGB tuples to a format compatible with Matplotlib
    colors = [(r / 255, g / 255, b / 255) for (r, g, b) in colors]

    # Create a scatter plot
    plt.scatter(reaction_time, range(len(reaction_time)), c=colors, marker='o', s=20)

    # Customize the plot
    plt.xlabel('Reaction Time')
    plt.ylabel('Data Point Index')
    plt.title('Reaction Time vs. Color')
    plt.colorbar(label='Color')

    # Save the plot to a file
    plt.savefig(output_filename)

plot_reaction_time_vs_color(attention, "attention_reaction_time_vs_color.png")
