import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


def extract_features(filename):
    match = re.search(r'(uint8|uint16|float32)/custom_data/(delta|repeats|outliers)_(\d+)', filename)
    if match:
        return match.groups()  # Returns a tuple with matched groups
    return (None, None, None)


def simplify_sprintz(data):
    data['Algorithm'] = data['Algorithm'].replace(
        {
            r'SprintzDelta(_16b)? -\d+': 'SprintzDelta',
            r'SprintzDelta_Huf(_16b)? -\d+': 'SprintzDelta_Huf'
        },
        regex=True
    )
    return data


def remove_algos(data):
    # Exclude specific algorithms
    algorithms_to_exclude = [
        'SprintzDelta -18', 'SprintzDelta_Huf -18', 'SprintzDelta_16b -18', 'SprintzDelta_Huf_16b -18',
        'SprintzDelta -1', 'SprintzDelta_Huf -1', 'SprintzDelta_16b -1', 'SprintzDelta_Huf_16b -1',
        'SprintzDelta -80', 'SprintzDelta_Huf -80', 'SprintzDelta_16b -80', 'SprintzDelta_Huf_16b -80'
    ]
    # Apply the filter to exclude the specified algorithms
    data = data[~data['Algorithm'].isin(algorithms_to_exclude)]
    return data


def algo_order(data):
    algorithm_order = ['LZ4', 'LZO -1', 'LZO -9',
                       'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
                       'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy'
                       ]
    data = data.copy()
    # Convert the Algorithm column to a categorical type with the specified order
    data['Algorithm'] = pd.Categorical(data['Algorithm'], categories=algorithm_order, ordered=True)
    return data


def algo_order_with_sprintz(data):
    algorithm_order = ['SprintzDelta','SprintzDelta_Huf', 'LZ4', 'LZO -1', 'LZO -9',
                       'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
                       'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy'
                       ]
    data = data.copy()
    # Convert the Algorithm column to a categorical type with the specified order
    data['Algorithm'] = pd.Categorical(data['Algorithm'], categories=algorithm_order, ordered=True)
    return data


def remove_files(data):
    # Exclude only files with specific filenames
    files_to_exclude = ['uci_gas.dat', 'msrc.dat', 'ucr.dat']
    data = data[~data['Filename'].str.contains('|'.join(files_to_exclude))]
    return data


def extract_datatype(data):
    data = data.copy()
    # Extracting DataType from the 'Filename' column
    data['DataType'] = data['Filename'].apply(lambda x: x.split('/')[1])
    return data


def remove_miniter(data):
    data = data[data['MinIters'] == 10]
    return data


def order_datasets():
    return ['uci_gas', 'msrc', 'ucr']



######################################################################### COMPRESSION RATIOS ##########################################################################################

def comp_ratio(data):
    # Simplify algorithm names
    data = simplify_sprintz(data)

    # Remove specific files and prepare data
    data = remove_files(data)
    data = extract_datatype(data)
    data = algo_order_with_sprintz(data)

    # Filter data to include only entries with 'None' in the 'Preprocs' column (no preprocessing)
    data = data[data['Preprocs'].isna()]

    # Define the order of datasets
    dataset_order = ['uci_gas', 'msrc', 'ucr']

    # Convert the Dataset column to a categorical type with the specified order
    data['Dataset'] = pd.Categorical(data['Dataset'], categories=dataset_order, ordered=True)

    # Group data by dataset
    grouped_data = data.groupby('Dataset', observed=False)

    datasets = data['Dataset'].unique()  # Adjust this column name based on your data

    algorithm_order = ['SprintzDelta', 'SprintzDelta_Huf', 'LZ4', 'LZO -1', 'LZO -9',
                       'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
                       'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy']
    data['Algorithm'] = pd.Categorical(data['Algorithm'], categories=algorithm_order, ordered=True)

    datatype_order = ['uint8', 'uint16', 'float32']
    data['DataType'] = pd.Categorical(data['DataType'], categories=datatype_order, ordered=True)

    # Define colors for each algorithm
    algorithm_colors = {
        'SprintzDelta': '#ff7f0e',  # Cyan
        'SprintzDelta_Huf': '#d62728',  # Red
        'LZ4': '#1f77b4',  # Blue
        'LZO -1': '#2ca02c',  # Green
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

    # Define the metric to plot
    metric = 'Ratio'  # Change to 'Compression speed' or 'Decompression speed' if needed

    # Loop over each dataset and create a separate plot
    for dataset in datasets:
        # Filter data for the current dataset
        dataset_data = data[data['Dataset'] == dataset]  # Adjust 'Dataset' column name based on your data

        # Group by DataType and Algorithm
        grouped = dataset_data.groupby(['DataType', 'Algorithm'], observed=False).agg({
            'Ratio': 'mean'
        }).reset_index()
        print("hier kommt grouped")
        print(grouped)
        # Initialize the plot
        fig, ax = plt.subplots(figsize=(12, 6))

        # Bar width
        bar_width = 0.06  # Smaller width to prevent overlap

        # Get unique data types and algorithms
        data_types = grouped['DataType'].unique()
        algorithms = grouped['Algorithm'].unique()

        # Set the positions of the bars
        bar_positions = np.arange(len(data_types))

        # Offset for bars to prevent overlapping
        offset = np.linspace(-bar_width * len(algorithms) / 2, bar_width * len(algorithms) / 2, len(algorithms))

        # Create bars for each Algorithm
        for i, algorithm in enumerate(algorithms):
            # Filter data for the current Algorithm
            algorithm_data = grouped[grouped['Algorithm'] == algorithm]

            # Plot bars for each data type with appropriate offset
            ax.bar(bar_positions + offset[i], algorithm_data[metric], width=bar_width, label=algorithm,
                   color=algorithm_colors[algorithm])

        # Customize the plot
        ax.set_xlabel('DataType', fontsize=17)
        ax.set_ylabel('Compression Ratio', fontsize=17)  # Change as needed for other metrics
        ax.set_xticks(bar_positions)
        ax.set_xticklabels(data_types, rotation=45, fontsize=17)
        ax.set_ylim(0, 100)
        ax.tick_params(axis='both', labelsize=17)

        handles, labels = ax.get_legend_handles_labels()
        legendFig = plt.figure("Legend plot", figsize=(8, 2))
        legendFig.legend(handles, labels, loc='upper center', ncols=6, bbox_to_anchor=(0.5, 1.0))
        legendFig.savefig('legend.png')
        legendFig.show()

        # Display or save the plot
        plt.tight_layout()
        # Uncomment the line below to save the plot as an image
        plt.savefig(f'{dataset}_compression_ratio.png')
        plt.show()

def comp_ratio_features(data):
    data = remove_miniter(data)
    data = data[data['Preprocs'] == 'None']
    data = simplify_sprintz(data)
    data = algo_order_with_sprintz(data)
    extracted_data = data['Filename'].apply(extract_features)
    data['DataType'], data['FeatureType'], data['FeatureValue'] = zip(*extracted_data)

    data.dropna(subset=['DataType', 'FeatureType', 'FeatureValue'], inplace=True)
    data['FeatureValue'] = data['FeatureValue'].astype(int)

    data = data[~((data['FeatureType'] == 'delta') & (data['FeatureValue'].isin([10000, 2000, 100])))]

    # Define colors for each algorithm
    colors = {
        'SprintzDelta': '#ff7f0e',  # Cyan
        'SprintzDelta_Huf': '#d62728',  # Red
        'LZ4': '#1f77b4',  # Blue
        'LZO -1': '#2ca02c',  # Green
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

    consistent_algorithm_order = ['SprintzDelta', 'SprintzDelta_Huf', 'LZ4', 'LZO -1', 'LZO -9',
                                  'Zstd -1', 'Zstd -9', 'Zlib -1', 'Zlib -9',
                                  'Brotli -1', 'Brotli -9', 'Huffman', 'Snappy']

    for feature_type in data['FeatureType'].unique():
        for data_type in data['DataType'].unique():
            # Set up the figure for each combination of FeatureType and DataType
            fig, ax = plt.subplots(figsize=(8, 6))

            subset = data[(data['DataType'] == data_type) & (data['FeatureType'] == feature_type)]
            subset = subset.sort_values(by='FeatureValue')

            # Plot each algorithm in the defined order with predefined colors
            for alg in consistent_algorithm_order:
                alg_data = subset[subset['Algorithm'] == alg]
                if not alg_data.empty:
                    ax.plot(alg_data['FeatureValue'], alg_data['Ratio'], marker='o', linestyle='-', linewidth=2,
                            color=colors[alg], label=alg)

            ax.set_xlabel(f'{feature_type.capitalize()} Value', fontsize=17)
            ax.set_ylabel('Compression Ratio', fontsize=17)
            ax.tick_params(axis='both', labelsize=17)
            ax.grid(True)
            ax.set_ylim(0, 110)

            handles, labels = ax.get_legend_handles_labels()
            legendFig = plt.figure("Legend plot", figsize=(8, 0.8))
            legendFig.legend(handles, labels, loc='upper center', ncol=6, bbox_to_anchor=(0.5, 1.0))
            legendFig.savefig(f'legend_ratio_feature_{data_type}.png')
            legendFig.show()

            # Adjust layout and save the figure
            plt.tight_layout()
            plt.savefig(f'{feature_type}_{data_type}_compression_ratio.png')
            plt.show()

def comp_ratio_preproc(data):
    # Extract datatype and preprocess the data
    data = extract_datatype(data)
    data = remove_miniter(data)
    data['Preprocs'] = data['Preprocs'].fillna('None')  # Assign 'None' if NaN
    data = remove_algos(data)
    data = remove_files(data)
    data = algo_order(data)

    # Define colors for each algorithm
    algorithm_colors = {
        'LZ4': '#1f77b4',  # Blue
        'LZO -1': '#2ca02c',  # Green
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

    # Group data for comparison by DataType
    grouped_data = data.groupby(['DataType'])

    # Iterate through each DataType and create individual plots for each Dataset within it
    for datatype, datatype_group in grouped_data:
        datasets = datatype_group['Dataset'].unique()

        for dataset in datasets:
            # Filter data for the current dataset
            dataset_group = datatype_group[datatype_group['Dataset'] == dataset]

            # Pivot data to get mean compression ratios for each preprocessing type
            pivot_data = dataset_group.groupby(['Preprocs', 'Algorithm'], observed=False)['Ratio'].mean().unstack('Algorithm')

            # Initialize a new figure for each dataset and data type
            fig, ax = plt.subplots(figsize=(12, 6))

            # Set the width of the bars and positions them
            bar_width = 0.05
            x = np.arange(len(pivot_data.index))  # Positions for each Preprocs group

            # Plot data
            for i, algorithm in enumerate(algorithm_colors.keys()):
                # Plot bars for each algorithm within each Preprocs group
                ax.bar(x + i * bar_width, pivot_data[algorithm], width=bar_width, color=algorithm_colors[algorithm], label=algorithm)

            # Customize the plot
            ax.set_xlabel('Preprocessing Method', fontsize=17)
            ax.set_ylabel('Compression Ratio', fontsize=17)
            ax.set_xticks(x + bar_width * (len(algorithm_colors) / 2))
            ax.set_xticklabels(pivot_data.index, rotation=45, ha='right', fontsize=17)
            ax.tick_params(axis='both', labelsize=17)
            ax.grid(True, which='both', axis='y', linestyle='--', alpha=0.5)
            ax.set_ylim(0, 100)


            # Adjust layout
            plt.tight_layout()

            # Save the plot
            plt.savefig(f'{dataset}_{datatype}_compression_ratios_preproc.png')
            plt.show()

    # Create a separate legend figure for better display
    handles, labels = ax.get_legend_handles_labels()
    legendFig = plt.figure("Legend plot", figsize=(8, 0.5))
    legendFig.legend(handles, labels, loc='upper center', ncol=6, bbox_to_anchor=(0.5, 1.0))
    legendFig.savefig('legend_preproc.png')
    legendFig.show()

def main_ratio_preproc():
    # Load the data
    file_path = '/experiments/merged_results.csv'
    data = pd.read_csv(file_path, low_memory=False)
    data = data[data['Algorithm'] != 'Memcpy']
    comp_ratio_preproc(data)

def main_ratio():
    # Load the data
    file_path = '/experiments/1_results_all_datasets/merged_results.csv'
    data = pd.read_csv(file_path, low_memory=False)
    data = data[data['Algorithm'] != 'Memcpy']
    comp_ratio(data)

def main_ratio_features():
    # Load the data
    file_path = '/experiments/5_results_features/merged_results.csv'
    data = pd.read_csv(file_path, low_memory=False)
    data = data[data['Algorithm'] != 'Memcpy']
    comp_ratio_features(data)

# Run the function
main_ratio_preproc()
main_ratio_features()
main_ratio()