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


### Installation

### Compilation

### Repository Structure

For Linux/MacOS/MinGW (Windows):
```
make
```

For 32-bit compilation:
```
make BUILD_ARCH=32-bit

```

<!-- lzbench was tested with:

- Ubuntu: gcc 4.6.3, 4.8.4 (both 32-bit and 64-bit), 4.9.3, 5.3.0, 6.1.1 and clang 3.4, 3.5, 3.6, 3.8
- MacOS: Apple LLVM version 6.0
- MinGW (Windows): gcc 5.3.0, 4.9.3 (32-bit), 4.8.3 (32-bit)
 -->

## Acknowledgments

This project builds upon the original lzbench benchmark and its predecessors. Special thanks to the open-source community for their contributions to the field of data compression.
