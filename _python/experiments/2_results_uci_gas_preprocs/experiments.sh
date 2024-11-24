#!/bin/sh

# Experiment 10: Delta Preprocessing
echo "Running Experiment 10: uci_gas with Delta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=uci_gas --miniters=1

# Experiment 11: Delta Preprocessing
echo "Running Experiment 11: uci_gas with Delta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=uci_gas --miniters=5

# Experiment 12: Delta Preprocessing
echo "Running Experiment 12: uci_gas with Delta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=uci_gas --miniters=10

# Experiment 13: DoubleDelta Preprocessing
echo "Running Experiment 13: uci_gas with DoubleDelta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=uci_gas --miniters=1

# Experiment 14: DoubleDelta Preprocessing
echo "Running Experiment 14: uci_gas with DoubleDelta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=uci_gas --miniters=5

# Experiment 15: DoubleDelta Preprocessing
echo "Running Experiment 15: uci_gas with DoubleDelta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=uci_gas --miniters=10