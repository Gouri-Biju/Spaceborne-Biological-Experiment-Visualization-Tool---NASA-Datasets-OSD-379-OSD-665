import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings
from django.shortcuts import render

# Sample data
data = [
    {
        'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI1',
        'Parameter Value: QA Score': '4.9 RNA Integrity Number',
        'Parameter Value: Fragment Size': '312 base pair',
        'Parameter Value: rRNA Contamination': '3.78 percent',
        'Parameter Value: Read Depth': '54477267 read',
        'Parameter Value: Spike-in Mix Number': 'Mix 1'
    },
    {
        'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI2',
        'Parameter Value: QA Score': '5.6 RNA Integrity Number',
        'Parameter Value: Fragment Size': '339 base pair',
        'Parameter Value: rRNA Contamination': '3.02 percent',
        'Parameter Value: Read Depth': '61115053 read',
        'Parameter Value: Spike-in Mix Number': 'Mix 1'
    },
    {
        'Sample Name': 'RR8_LVR_BSL_ISS-T_OLD_BI3',
        'Parameter Value: QA Score': '6.6 RNA Integrity Number',
        'Parameter Value: Fragment Size': '332 base pair',
        'Parameter Value: rRNA Contamination': '1.53 percent',
        'Parameter Value: Read Depth': '63712483 read',
        'Parameter Value: Spike-in Mix Number': 'Mix 1'
    }
]

# Convert the dataset to a DataFrame
df = pd.DataFrame(data)

# Extract numeric values from the string columns
df['QA Score'] = df['Parameter Value: QA Score'].str.extract(r'(\d+\.\d+)').astype(float)
df['Fragment Size'] = df['Parameter Value: Fragment Size'].str.extract(r'(\d+)').astype(int)
df['rRNA Contamination'] = df['Parameter Value: rRNA Contamination'].str.extract(r'(\d+\.\d+)').astype(float)
df['Read Depth'] = df['Parameter Value: Read Depth'].str.extract(r'(\d+)').astype(int)

# Function to save the plot as an image in the specified path
def save_plot_as_image(filename):
    # Create the full path to the 'images' folder inside your STATICFILES_DIRS
    image_folder = os.path.join(settings.STATICFILES_DIRS[0], 'images')

    # Create the directory if it doesn't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # Generate the full path to save the image
    image_path = os.path.join(image_folder, filename)

    # Save the plot to the generated path
    plt.savefig(image_path, format='png')
    plt.close() # Close the plot after saving to free up memory

def plot_view(request):
    # Plot 1: Bar Plot of RNA Integrity Number (QA Score) per Sample
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Sample Name', y='QA Score', data=df)
    plt.title('RNA Integrity (QA Score) per Sample')
    plt.xlabel('Sample Name')
    plt.ylabel('RNA Integrity (QA Score)')
    plt.xticks(rotation=45)
    save_plot_as_image('bar_chart.png')  # Save the plot as bar_chart.png

    # Plot 2: Scatter Plot of Read Depth vs rRNA Contamination
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Read Depth', y='rRNA Contamination', data=df, s=100, color="b")
    plt.title('Read Depth vs rRNA Contamination')
    plt.xlabel('Read Depth')
    plt.ylabel('rRNA Contamination (%)')
    save_plot_as_image('scatter_plot.png')  # Save the plot as scatter_plot.png

    # Plot 3: Box Plot of Fragment Size per Sample
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Sample Name', y='Fragment Size', data=df)
    plt.title('Fragment Size Distribution per Sample')
    plt.xlabel('Sample Name')
    plt.ylabel('Fragment Size (base pairs)')
    plt.xticks(rotation=45)
    save_plot_as_image('box_plot.png')  # Save the plot as box_plot.png

    # Plot 4: Violin Plot of Spike-in Mix Number vs rRNA Contamination
    plt.figure(figsize=(8, 5))
    sns.violinplot(x='Parameter Value: Spike-in Mix Number', y='rRNA Contamination', data=df)
    plt.title('Spike-in Mix Number vs rRNA Contamination')
    plt.xlabel('Spike-in Mix Number')
    plt.ylabel('rRNA Contamination (%)')
    save_plot_as_image('violin_plot.png')  # Save the plot as violin_plot.png

    # Plot 5: Distribution of rRNA Contamination
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rRNA Contamination'], kde=True)
    plt.title('rRNA Contamination Distribution')
    plt.xlabel('rRNA Contamination (%)')
    plt.ylabel('Frequency')
    save_plot_as_image('histogram_plot.png')  # Save the plot as histogram_plot.png

    # Pass the file names to the template for rendering
    return render(request, 'graphs.html', {
        'bar_chart': 'images/bar_chart.png',
        'scatter_plot': 'images/scatter_plot.png',
        'box_plot': 'images/box_plot.png',
        'violin_plot': 'images/violin_plot.png',
        'histogram_plot': 'images/histogram_plot.png'
    })
