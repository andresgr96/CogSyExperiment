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
    plt.xlim((0,5))
    # Save the plot to a file
    plt.savefig(output_filename)

## Doesnt work yet and its useless rn 

# def rgb_string_to_tuple(rgb_string):
#     # Expected format: "(R, G, B)"
#     try:
#         rgb_string = rgb_string.strip("()").replace(" ", "")
#         r, g, b = map(int, rgb_string.split(","))
#         return (r, g, b)
#     except (ValueError, AttributeError):
#         return None

# def bar_plot(data, output_filename):
#     # Safely convert the Color column
#     data['Color'] = data['Color'].apply(lambda x: ast.literal_eval(x)) #apply(rgb_string_to_tuple)

#     # Drop rows with missing or malformed Color values
#     data = data.dropna(subset=['Color'])

#     # Extract Reaction Time and Color columns
#     reaction_time = data['Reaction_Time']
#     colors = data['Color']

#     # Convert RGB tuples to a format compatible with Matplotlib
#     colors = [(r / 255, g / 255, b / 255) for (r, g, b) in colors]

#     # Create a bar chart
#     plt.bar(range(len(reaction_time)), reaction_time, color=colors)

#     # Customize the bar chart
#     plt.xlabel('Data Point Index')
#     plt.ylabel('Reaction Time')
#     plt.title('Reaction Time vs. Color')
#     plt.xticks(range(len(reaction_time)), [str(i) for i in range(len(reaction_time))], rotation=90)
#     # plt.colorbar(label='Color')

#     # Save the bar chart to a file
#     plt.savefig(output_filename)

def plot_memory_data(data, output_filename):
    # Convert the Color column from RGB strings to tuples
    data['Color'] = data['Color'].apply(lambda x: ast.literal_eval(x))

    # Group data by Number Shown and Correct
    grouped_data = data.groupby(['Number_Shown', 'Correct'])

    # Count the occurrences of True and False for Correct
    correct_counts = grouped_data.size().unstack()

    # Fill any missing values with zeros
    correct_counts = correct_counts.fillna(0)

    # Plot a bar chart
    correct_counts.plot(kind='bar', stacked=True, colormap='Paired')

    # Customize the bar chart
    plt.xlabel('Number Shown')
    plt.ylabel('Count')
    plt.title('Correct vs. Number Shown with RGB Color')
    plt.legend(title='Correct', loc='upper right')

    # Save the plot to a file
    plt.savefig(output_filename)

plot_reaction_time_vs_color(attention, "attention_reaction_time_vs_color.png")
plot_memory_data(memory, "memory_correct_vs_number_shown.png")
