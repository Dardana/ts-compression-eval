#!/bin/sh

# Initialize datasets
python3 -m _python.datasets.compress_bench

# Experiment 1
echo "Running Experiment 1: uci_gas with 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=uci_gas --miniters=1

# Experiment 2
echo "Running Experiment 2: uci_gas with 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=uci_gas --miniters=5

# Experiment 3
echo "Running Experiment 3: uci_gas with 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=uci_gas --miniters=10

# Experiment 4
echo "Running Experiment 4: msrc with 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=msrc --miniters=1

# Experiment 5
echo "Running Experiment 5: msrc with 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=msrc --miniters=5

# Experiment 6
echo "Running Experiment 6: msrc with 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=msrc --miniters=10

# Experiment 7
echo "Running Experiment 7: ucr with 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=ucr --miniters=1

# Experiment 8
echo "Running Experiment 8: ucr with 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=ucr --miniters=5

# Experiment 9
echo "Running Experiment 9: ucr with 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --dsets=ucr --miniters=10