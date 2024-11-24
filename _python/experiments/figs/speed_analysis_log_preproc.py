import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Load and prepare the data
data = pd.read_csv('/experiments/merged_results.csv')
data = data[data['Algorithm'] != 'Memcpy']
data['Preprocs'] = data['Preprocs'].fillna('None')
data['DataType'] = data['Filename'].apply(lambda x: x.split('/')[1])

algorithms_to_exclude = [
        'SprintzDelta -18', 'SprintzDelta_Huf -18', 'SprintzDelta_16b -18', 'SprintzDelta_Huf_16b -18',
        'SprintzDelta -1', 'SprintzDelta_Huf -1', 'SprintzDelta_16b -1', 'SprintzDelta_Huf_16b -1',
        'SprintzDelta -80', 'SprintzDelta_Huf -80', 'SprintzDelta_16b -80', 'SprintzDelta_Huf_16b -80'
    ]
# Apply the filter to exclude the specified algorithms
data = data[~data['Algorithm'].isin(algorithms_to_exclude)]

# Define orders and categories
algorithm_order = ['LZ4', 'LZO -1', 'LZO -9',
    'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
    'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy'
]

data = data.copy()
    # Convert the Algorithm column to a categorical type with the specified order
data['Algorithm'] = pd.Categorical(data['Algorithm'], categories=algorithm_order, ordered=True)

datasets_order = ['uci_gas', 'msrc', 'ucr']
preprocessing_types = ['Delta', 'DoubleDelta', 'None']
datatypes = data['DataType'].unique()  # Extract unique datatypes from your data

# Group and calculate means for Compression and Decompression Speed by dataset, datatype, algorithm, and preprocessing type
aggregated_data = data.groupby(['Dataset', 'DataType', 'Algorithm', 'Preprocs']).agg({
    'Compression speed': 'mean',
    'Decompression speed': 'mean'
}).reset_index()

aggregated_data.to_csv('Results_speed_preproc.csv', sep=',', index=False)

# Set plot dimensions and other constants
global_min = -10 ** 5  # accommodate for negative decompression speeds
global_max = 10 ** 5

colors = {
    'Delta': {'compression': '#1f77b4', 'decompression': '#aec7e8'},   # Blue
    'DoubleDelta': {'compression': '#ff7f0e', 'decompression': '#ffbb78'},  # Orange
    'None': {'compression': '#2ca02c', 'decompression': '#98df8a'}  # Green
}
# Iterating over datasets and datatypes for individual plots
for dataset in datasets_order:
    for datatype in datatypes:
        fig, ax = plt.subplots(figsize=(14, 8))
        positions = np.arange(len(algorithm_order))

        # Plot each preprocessing type with an offset
        bar_width = 0.3
        offset = -bar_width * len(preprocessing_types) / 2

        for i, preprocessing in enumerate(preprocessing_types):
            subset = aggregated_data[(aggregated_data['Dataset'] == dataset) &
                                     (aggregated_data['DataType'] == datatype) &
                                     (aggregated_data['Preprocs'] == preprocessing)]

            # Adjust the positions for each preprocessing type
            adjusted_positions = positions + i * bar_width + offset

            ax.bar(adjusted_positions, subset['Compression speed'], width=bar_width,color=colors[preprocessing]['compression'], label=f'{preprocessing} - Compression', alpha=0.8)
            ax.bar(adjusted_positions, -subset['Decompression speed'], width=bar_width,color=colors[preprocessing]['decompression'], label=f'{preprocessing} - Decompression', alpha=0.8)

        ax.set_xlabel('Algorithm', fontsize=25)
        ax.set_ylabel('Speed (MB/s)', fontsize=25)
        ax.set_ylim(global_min, global_max)
        ax.set_xticks(positions)
        ax.set_xticklabels(algorithm_order, rotation=45, ha='right',fontsize=25)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.tick_params(axis='both', labelsize=25)
        ax.set_yscale('symlog')
        ax.grid(True, which='both', axis='y', linestyle='--', alpha=0.5)


        def custom_format_func(value, tick_number):
            if value != 0:
                return f"$10^{{{int(np.log10(abs(value)))}}}$"
            else:
                return "0"


        ax.yaxis.set_major_formatter(ticker.FuncFormatter(custom_format_func))
        #ax.legend()

        plt.savefig(f"{dataset}_{datatype}_Speed_Analysis.png", bbox_inches='tight')
        plt.show()

handles, labels = ax.get_legend_handles_labels()
legendFig = plt.figure("Legend plot", figsize=(8, 0.5))
legendFig.legend(handles, labels, loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.0))
legendFig.savefig('legend_speed_proc.png')
legendFig.show()
