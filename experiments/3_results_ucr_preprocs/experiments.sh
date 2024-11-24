#!/bin/sh

# Experiment 16: Delta Preprocessing
echo "Running Experiment 16: ucr with Delta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=ucr --miniters=1

# Experiment 17: Delta Preprocessing
echo "Running Experiment 17: ucr with Delta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=ucr --miniters=5

# Experiment 18: Delta Preprocessing
echo "Running Experiment 18: ucr with Delta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=Delta --dsets=ucr --miniters=10

# Experiment 19: DoubleDelta Preprocessing
echo "Running Experiment 19: ucr with DoubleDelta preprocessing and 1 miniter"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=ucr --miniters=1

# Experiment 20: DoubleDelta Preprocessing
echo "Running Experiment 20: ucr with DoubleDelta preprocessing and 5 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=ucr --miniters=5

# Experiment 21: DoubleDelta Preprocessing
echo "Running Experiment 21: ucr with DoubleDelta preprocessing and 10 miniters"
python3 -m _python.main --sweep algos=SprintzDelta,SprintzDelta_16b,SprintzDelta_Huf,SprintzDelta_Huf_16b,Zlib,Zstd,LZ4,LZO,Huffman,Snappy,Brotli --preprocs=DoubleDelta --dsets=ucr --miniters=10