#!/bin/sh

# Experiment 22: Delta Preprocessing
echo "Running Experiment 22: msrc with Delta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=msrc --miniters=1

# Experiment 23: Delta Preprocessing
echo "Running Experiment 23: msrc with Delta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=msrc --miniters=5

# Experiment 24: Delta Preprocessing
echo "Running Experiment 24: msrc with Delta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=msrc --miniters=10

# Experiment 25: DoubleDelta Preprocessing
echo "Running Experiment 25: msrc with DoubleDelta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=msrc --miniters=1

# Experiment 26: DoubleDelta Preprocessing
echo "Running Experiment 26: msrc with DoubleDelta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=msrc --miniters=5

# Experiment 27: DoubleDelta Preprocessing
echo "Running Experiment 27: msrc with DoubleDelta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=msrc --miniters=10