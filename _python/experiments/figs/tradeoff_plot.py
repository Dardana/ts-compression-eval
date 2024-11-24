

import pandas as pd
import plots
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Load your data
file_path = '/experiments/1_results_all_datasets/merged_results.csv'
data = pd.read_csv(file_path, low_memory=False)

# Filtering the data according to your criteria
data = data[data['Algorithm'] != 'Memcpy']
data = data[data['Algorithm'] != 'LZO -1']
data = data[data['MinIters'] == 10]

data = plots.simplify_sprintz(data)
data = plots.remove_files(data)
data = plots.extract_datatype(data)
algorithm_order = ['SprintzDelta','SprintzDelta_Huf', 'LZ4', 'LZO -9',
                       'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
                       'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy'
                       ]
data = data.copy()
data['Algorithm'] = pd.Categorical(data['Algorithm'], categories=algorithm_order, ordered=True)


# Group the data by DataType
data_types = data['DataType'].unique()

# Custom colors for each algorithm
colors = {
    'SprintzDelta': '#ff7f0e',  # Cyan
    'SprintzDelta_Huf': '#d62728',  # Red
    'LZ4': '#1f77b4',  # Blue
    'LZO -9': '#ff1493',  # Deep Pink
    'Zstd -1': '#e377c2',  # Pink
    'Zstd -9': '#8c564b',  # Brown
    'Zlib -1': '#00ff00',  # Lime
    'Zlib -9': '#ff00ff',  # Orangeff00ff
    'Brotli -1': '#7f7f7f',  # Gray
    'Brotli -9': '#bcbd22',  # Olive
    'Huffman': '#9467bd',  # Purple
    'Snappy': '#17becf'  # Magenta
}

# Define the metrics
categories = ['Compression speed', 'Decompression speed', 'Ratio']
num_vars = len(categories)

# Create the angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

def normalize(column):
    return (column - column.min()) / (column.max() - column.min())

# Loop over each DataType and create a radar chart
for dtype in data_types:
    # Filter data for the current DataType
    dtype_data = data[data['DataType'] == dtype]

    # Aggregate the data by Algorithm for the current DataType
    aggregated_data = dtype_data.groupby(['Algorithm'], observed=False).agg({
        'Compression speed': 'mean',
        'Decompression speed': 'mean',
        'Ratio': 'mean'
    }).reset_index()
    aggregated_data.to_csv(f'{dtype}_Results_speed.csv', sep=',', index=False)

    # Normalizing the data using Min-Max normalization
    normalized_data = aggregated_data.copy()
    normalized_data['Compression speed'] = normalize(aggregated_data['Compression speed'])
    normalized_data['Decompression speed'] = normalize(aggregated_data['Decompression speed'])
    normalized_data['Ratio'] = normalize(aggregated_data['Ratio'])

    # Initialize the radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    ax.spines['polar'].set_visible(False)

    # Plot each algorithm with the corresponding color
    for i, (index, row) in enumerate(normalized_data.iterrows()):
        # Data for this algorithm
        values = row[categories].tolist()
        values += values[:1]

        # Plot
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=row['Algorithm'],
                color=colors.get(row['Algorithm'], '#000000'))

    # Set the labels and title
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(['CS', 'DS', 'Ratio'], fontsize=17)
    ax.set_yticklabels([], fontsize=17)


    # Annotate the circles with corresponding values
    num_circles = 5  # Number of concentric circles
    for i in range(1, num_circles + 1):
        value = i / num_circles
        ax.text(pi / 2, value, f'{value:.1f}', horizontalalignment='center', verticalalignment='bottom', fontsize=17)

    plt.savefig(f"{dtype}_trade_off.png")
    plt.show()

handles, labels = ax.get_legend_handles_labels()
legendFig = plt.figure("Legend trade_off", figsize=(8, 0.5))
legendFig.legend(handles, labels, loc='upper center', ncol=6, bbox_to_anchor=(0.5, 1.0))
legendFig.savefig('legend_trade_off.png')
legendFig.show()
