# Time Series Compression Benchmark for Thesis Reproduction 

This repository contains the code and instructions needed to reproduce the results presented in my master's thesis: **'A Comprehensive Analysis and Evaluation of Lossless Compression Techniques for Time Series Data'**.

This repository is a fork of the [Sprintz benchmark](https://github.com/dblalock/lzbench), itself derived from the [original lzbench](https://github.com/inikep/lzbench). 

The original 'lzbench' is an in-memory benchmark of open-source LZ77/LZSS/LZMA compressors. It joins all compressors into a single executable. At the beginning an input file is read to memory. Then all compressors are used to compress and decompress the file and decompressed file is verified.
This approach has a big advantage of using the same compiler with the same optimizations for all compressors. The disadvantage is that it requires source code of each compressor (therefore Slug or lzturbo are not included).

The Sprintz fork added new functionality, specifically enabling integrated [double-]delta coding and the execution of simple queries on data after decompression.

## Enhancements in This Fork
This fork further extends the capabilities of the Sprintz benchmark with several key features aimed specifically at evaluating lossless compression techniques for time series data:
- **Integrated Float Compression**: This fork introduces the ability to benchmark compression algorithms on float datasets, which is crucial for evaluating the performance of compressors on time series data commonly represented as floating-point numbers.
-  **Custom Data for Analysis**: Added custom datasets specifically designed to analyze the impact of data features (such as repeats, deltas and outliers) on compression performance. This feature enables users to evaluate how different data characteristics affect the efficiency of various compression algorithms.
- **Enhanced Evaluation Framework**: Built to align with the experimental setup of the master's thesis, this fork allows for a comprehensive comparison of various lossless compression algorithms, both general-purpose and specialized for time series data.

## Reproduction of Results

### Prerequisites
- **X86 Architecture**: This project requires an X86 architecture to run. It is not compatible with ARM or other architectures at this time.
  
### Dependencies
- **Make**: Required to build the project.
- **Clang**: Ensure you have Clang installed as the code depends on it for compilation.
- **Joblib**: For caching function output.
- **Pandas**: For storing results and reading in data.
- **Matplotlib**: For plotting, if you want to reproduce the figures.
- **Numpy**: Required for numerical computations and handling datasets.

### Datasets
- **MSRC-12**: Kinect readings as subjects performed various actions. Link: [MSRC-12 Dataset](https://www.microsoft.com/en-us/download/details.aspx?id=52283?from=https://research.microsoft.com/en-us/um/cambridge/projects/msrc12/&type=exact)
- **UCI Gas**: Measurements of gas concentrations over time. Link: [UCI Gas Dataset](https://archive.ics.uci.edu/dataset/322/gas+sensor+array+under+dynamic+gas+mixtures)  
- **UCR Archive**: A collection of 85 time series datasets. Link: [UCR Archive](https://www.cs.ucr.edu/~eamonn/time_series_data/)  
- **Synthetic Dataset**: Features like repeats, deltas, and outliers. Code to generate this dataset can be found in `_python/generate_datasets.py`.

### Run Experiments
1. Clone this repository:
```
git clone https://github.com/Dardana/ts-compression-eval.git
``` 
2. Navigate to the repository:
```
cd ts-compression-benchmark
```
3. Compile the project:
```
make
```
4. Obtain datasets: 
Download the datasets listed above and generate the synthetic dataset using the provided script. The datasets need to be saved in the following directory structure:
```
datasets
│  
└───custom_data
│   
└───MSRC-12
│   
└───uci-gas-sensor
│   
└───UCR_TS_Archive_2015
```
Or you can download the entire `datasets` folder directly from this [link](#). 
Once you obtain the folder, place the folder in your desired directory. 

5. Change the dataset directory in `_python/datasets/paths.py` to match the location of your `datasets` folder.
For example: 
```
/root/datasets
```
7. Initialize datasets from `ts-compression-benchmark`:
```
python3 -m _python.datasets.compress_bench
```
8. Run different experiments found in `_python/experiments`.

## Acknowledgments

This project builds upon the original lzbench benchmark and its predecessors. Special thanks to the open-source community for their contributions to the field of data compression.
