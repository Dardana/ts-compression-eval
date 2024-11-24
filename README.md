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

## Getting Started
### Prerequisites
- **Make**: Required to build the project.
- **Clang**: Ensure you have Clang installed as the code depends on it for compilation.
- **X86 Architecture**: This project requires an X86 architecture to run. It is not compatible with ARM or other architectures at this time.

### Installation
1. Clone this repository:
```
git clone https://github.com/Dardana/ts-compression-eval.git
``` 
2. Navigate to the repository:
```
cd ts-compression-benchmark
``` 
### Compilation
To compile the project, simply run:
```
make
```
Ensure that both `make` and `clang` are installed on your system for the compilation process to work properly.
### Repository Structure

## Acknowledgments

This project builds upon the original lzbench benchmark and its predecessors. Special thanks to the open-source community for their contributions to the field of data compression.
