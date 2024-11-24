#!/bin/sh

# Initialize datasets
python3 -m _python.datasets.compress_bench

# Experiment 28
echo "Running Experiment 28: custom_data with 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=custom_data --miniters=1

# Experiment 29
echo "Running Experiment 29: custom_data with 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=custom_data --miniters=5

# Experiment 30
echo "Running Experiment 30: custom_data with 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=custom_data --miniters=10

# Experiment 31: Delta Preprocessing
echo "Running Experiment 31: custom_data with Delta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=custom_data --miniters=1

# Experiment 32: Delta Preprocessing
echo "Running Experiment 32: custom_data with Delta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=custom_data --miniters=5

# Experiment 33: Delta Preprocessing
echo "Running Experiment 33: custom_data with Delta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=custom_data --miniters=10

# Experiment 34: DoubleDelta Preprocessing
echo "Running Experiment 34: custom_data with DoubleDelta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=custom_data --miniters=1

# Experiment 35: DoubleDelta Preprocessing
echo "Running Experiment 35: custom_data with DoubleDelta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=custom_data --miniters=5

# Experiment 36: DoubleDelta Preprocessing
echo "Running Experiment 36: custom_data with DoubleDelta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=custom_data --miniters=10