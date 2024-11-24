import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Load the data
file_path = '/experiments/1_results_all_datasets/merged_results.csv'
data = pd.read_csv(file_path)

# Remove text after the algorithm names using regex and simplify algorithm names
data['Algorithm'] = data['Algorithm'].replace(
    {
        r'SprintzDelta(_16b)? -\d+': 'SprintzDelta',
        r'SprintzDelta_Huf(_16b)? -\d+': 'SprintzDelta_Huf'
    },
    regex=True
)

# Remove 'memcpy' entries
data = data[~data['Algorithm'].str.contains('Memcpy', case=False)]

# Filter data for MinIters = 10
data = data[data['MinIters'] == 10]

# Exclude specific files
files_to_exclude = ['uci_gas.dat', 'ucr.dat', 'msrc.dat']
data = data[~data['Filename'].str.contains('|'.join(files_to_exclude))]

# Extract the data type from the Filename (assuming filename contains the data type)
data['DataType'] = data['Filename'].str.extract(r'(uint8|uint16|float32)', expand=False)

# Specify the desired order of algorithms
algorithm_order = [
    'SprintzDelta', 'SprintzDelta_Huf', 'LZ4', 'LZO -1', 'LZO -9',
    'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
    'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy'
]

# Convert the Algorithm column to a categorical type with the specified order
data['Algorithm'] = pd.Categorical(data['Algorithm'], categories=algorithm_order, ordered=True)

# Group by Dataset, Algorithm, and DataType to calculate the mean compression and decompression speeds
aggregated_data = data.groupby(['Dataset', 'Algorithm', 'DataType'], observed=False).agg({
    'Compression speed': 'mean',
    'Decompression speed': 'mean'
}).reset_index()
aggregated_data.to_csv('Results_speed.csv', sep=',', index=False)
# Define colors for each data type
colors = {
    'float32': {'compression': '#1f77b4', 'decompression': '#aec7e8'},   # Blue
    'uint16': {'compression': '#ff7f0e', 'decompression': '#ffbb78'},  # Orange
    'uint8': {'compression': '#2ca02c', 'decompression': '#98df8a'}  # Green
}

# Set consistent y-axis limits
global_min = -10 ** 5  # To accommodate negative decompression speeds
global_max = 10 ** 5   # Maximum y-axis limit for compression speeds

# Define the order of datasets for separate plots
datasets_order = ['uci_gas', 'msrc', 'ucr']

# Plot Compression and Decompression Speed separately for each dataset and data type
for dataset in datasets_order:
    subset = aggregated_data[aggregated_data['Dataset'] == dataset].copy()

    # Initialize the figure for each dataset
    fig, ax = plt.subplots(figsize=(12, 8))

    # Set the width of the bars and position them
    bar_width = 0.3
    x = range(len(algorithm_order))

    for j, dtype in enumerate(['float32', 'uint16', 'uint8']):
        dtype_subset = subset[subset['DataType'] == dtype]

        # Create a new column for negative decompression speed
        dtype_subset = dtype_subset.copy()
        dtype_subset.loc[:, 'Negative Decompression speed'] = -dtype_subset['Decompression speed']

        # Plot Compression Speed (positive)
        ax.bar(
            [p + j * bar_width for p in x],
            dtype_subset['Compression speed'],
            color=colors[dtype]['compression'],
            width=bar_width,
            label=f'Compression Speed ({dtype})'
        )

        # Plot Decompression Speed (negative)
        ax.bar(
            [p + j * bar_width for p in x],
            dtype_subset['Negative Decompression speed'],
            color=colors[dtype]['decompression'],
            width=bar_width,
            label=f'Decompression Speed ({dtype})',
            alpha=0.9
        )

    # Customize the plot
    ax.set_xlabel('Algorithm', fontsize=25)
    ax.set_ylabel('Speed (MB/s)', fontsize=25)
    ax.set_ylim(global_min, global_max)

    # Set ticks and labels
    ax.set_xticks([p + bar_width for p in x])
    ax.set_xticklabels(algorithm_order, rotation=45, ha='right', fontsize=25)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_yscale('symlog')
    ax.tick_params(axis='both', labelsize=25)


    def custom_format_func(value, tick_number):
        if value != 0:
            return f"$10^{{{int(np.log10(abs(value)))}}}$"
        else:
            return "0"


    ax.yaxis.set_major_formatter(ticker.FuncFormatter(custom_format_func))
    # Add grid to the plot
    ax.grid(True, which='both', axis='y', linestyle='--', alpha=0.5)


    # Add legend to the plot
    #ax.legend(loc='upper left', fontsize=14, bbox_to_anchor=(1.05, 1))

    # Save the figure for each dataset
    plt.tight_layout()
    plt.savefig(f"{dataset}_Compression_Decompression_Speed_Analysis_log.png", bbox_inches='tight')

    # Display the plot
    plt.show()

handles, labels = ax.get_legend_handles_labels()
legendFig = plt.figure("Legend plot", figsize=(8, 0.5))
legendFig.legend(handles, labels, loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.0))
legendFig.savefig('legend_speed.png')
legendFig.show()
