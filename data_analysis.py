import matplotlib.pyplot as plt
import ast
from merge_csv import merge_csv
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as mcolors
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
    # plt.bar(range(len(reaction_time)), reaction_time, color=colors)
    # Customize the plot
    plt.xlabel('Reaction Time')
    plt.ylabel('Data Point Index')
    plt.title('Reaction Time vs. Color')
    plt.colorbar(label='Color')
    plt.xlim((0,5))
    # Save the plot to a file
    plt.savefig(output_filename)

def bar_plot(data, output_filename):
    # Convert the Color column from string to tuple
    data['Color'] = data['Color'].apply(lambda x: ast.literal_eval(x))

    # Extract Reaction Time and Color columns
    reaction_time = data['Reaction_Time']
    colors = data['Color']

    # Convert RGB tuples to a format compatible with Matplotlib
    colors = [(r / 255, g / 255, b / 255) for (r, g, b) in colors]

    # plt.savefig(output_filename)
    normed_reaction_time = (reaction_time - min(reaction_time)) / (max(reaction_time) - min(reaction_time))
    
    # Map the normalized reaction times to colors using the viridis colormap
    cmap = cm.viridis
    colors = cmap(normed_reaction_time)

    bars = plt.bar(reaction_time, range(len(reaction_time)), color=colors, width=1.5) # Adjusted width here
    
    # Create a mappable object for the colorbar
    norm = mcolors.Normalize(vmin=min(reaction_time), vmax=max(reaction_time))
    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Customize the plot
    plt.xlabel('Data Point Index')
    plt.ylabel('Reaction Time')
    plt.title('Reaction Time vs. Color')
    plt.colorbar(sm, label='Reaction Time')  # Adjusted label here
    plt.ylim(0, 20)  # Adjusted to be

    # Save the plot to a file
    plt.savefig(output_filename)
    plt.show()
    
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

def string_to_rgb(color_str):
    r, g, b = map(int, color_str.strip("()").split(","))
    return r, g, b




def scatter_plotly(data, output_filename):
    # Extract Reaction Time and Color columns
    reaction_time = data['Reaction_Time']
    colors = data['Color']

    # Convert RGB tuples to a format compatible with Plotly
    colors = [string_to_rgb(color_str) for color_str in colors]
    colors = [(r / 255, g / 255, b / 255) for (r, g, b) in colors]

    # Create the scatter plot
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=list(range(len(reaction_time))),  # Index
            y=reaction_time,  # Reaction time
            mode='markers',
            marker=dict(
                color=colors,  # Set color to the RGB values
                size=10  # Adjust size as needed
            )
        )
    )

    # Customize the plot
    fig.update_layout(
        title='Reaction Time vs. Color',
        xaxis_title='Data Point Index',
        yaxis_title='Reaction Time',
        yaxis=dict(range=[0, 5])
    )

    # Save the plot to a file
    fig.write_image(output_filename)
    fig.show()

# Example usage:
# scatter_plotly(attention, 'scatter_plot.png')
def to_grayscale(color):
    return 0.2989 * color[0] + 0.5870 * color[1] + 0.1140 * color[2]
    
def memory_acc_color(df, output_filename):
    df['Color'] = df['Color'].apply(lambda x: ast.literal_eval(x))
    df['Grayscale Value'] = df['Color'].apply(to_grayscale)
    colormap = mcolors.LinearSegmentedColormap.from_list("grayscale", ["black", "white"])
    # Plot
    fig, ax = plt.subplots()
    for _, row in df.iterrows():
        ax.scatter(row['Number_Shown'], row['Grayscale Value'], c=[row['Grayscale Value']], 
               cmap=colormap, edgecolors='green' if row['Correct'] else 'red', linewidths=2)
    ax.set_xlabel('Number Shown')
    ax.set_ylabel('Grayscale Value')
    ax.set_title('Number Shown vs Color')
    plt.xticks(range(int(min(df['Number_Shown'])), int(max(df['Number_Shown'])) + 1, 1))
    plt.show()

    # Convert RGB tuples to a format compatible with Matplotlib
    # df['Y_value'] = df['Color'].apply(lambda x: x[0])

    # colors = df['Color']
    # colors = [(r / 255, g / 255, b / 255) for (r, g, b) in colors]
    

    # fig, ax = plt.subplots()
    
    # # Plot each data point one by one, changing the marker based on the 'Correct' value
    # for x, y, c, correct in zip(df['Number_Shown'], df['Y_value'], colors, df['Correct']):
    #     edgecolor = 'green' if correct else 'red'
    #     ax.scatter(x, y, c=[c], s=100, edgecolor=edgecolor, linewidths=1.5)

    # ax.set_xlabel('Number Shown')
    # ax.set_ylabel('Data Point Index')
    # ax.set_title('Number Shown vs Color')
    # plt.show()

    # df['Color'] = df['Color'].apply(lambda x: ast.literal_eval(x))
    # colors = df['Color']

    # # Convert RGB tuples to a format compatible with Matplotlib
    
    # colors = [(r / 255, g / 255, b / 255) for (r, g, b) in colors]
    # y_values = range(len(df))

    # fig, ax = plt.subplots()
    
    # # Plot each data point one by one, changing the marker based on the 'Correct' value
    # for i, (x, y, c, correct) in enumerate(zip(df['Number_Shown'], y_values, colors, df['Correct'])):
    #     edgecolor = 'green' if correct else 'red'
    #     ax.scatter(x, y, c=[c], s=100, edgecolor=edgecolor, linewidths=1.5)

    # ax.set_xlabel('Number Shown')
    # ax.set_ylabel('Data Point Index')
    # ax.set_title('Number Shown vs Color')
    # plt.show()

def average_bar_plot(data, output_filename):
    # Convert the Color column from string to tuple
    data['Color'] = data['Color'].apply(lambda x: ast.literal_eval(x))

    # Group the data by 'Color' and calculate the average reaction time for each color
    color_avg_reaction_time = data.groupby('Color')['Reaction_Time'].mean()

    # Extract unique colors and their corresponding average reaction times
    unique_colors = color_avg_reaction_time.index
    avg_reaction_times = color_avg_reaction_time.values

    # Convert RGB tuples to a format compatible with Matplotlib
    colors = [(r / 255, g / 255, b / 255) for (r, g, b) in unique_colors]

    # Create a barplot
    plt.bar(range(len(unique_colors)), avg_reaction_times, color=colors)

    # Customize the plot
    plt.xlabel('Color')
    plt.ylabel('Reaction Time')
    plt.title('Average Reaction Time per Color')

    # Set the x-axis ticks and labels to match the unique colors
    # plt.xticks(range(len(unique_colors)), unique_colors, rotation=45, ha='right')

    # Save the plot to a file
    plt.savefig(output_filename)
    plt.show()
   
# plot_reaction_time_vs_color(attention, "attention_reaction_time_vs_color.png")
# bar_plot(attention, "bar_plot.png")
# plot_memory_data(memory, "memory_correct_vs_number_shown.png")
# memory_acc_color(memory, "memory_acc_color.png")
average_bar_plot(attention, "average_reaction_time_vs_color.png")
