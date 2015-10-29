#!/bin/bash
time ./compress_fasta_hil.py tair8.fasta tair9.fasta hilbert.csv
./x265_mod --input output.yuv --input-res 4096x4096 --fps 2 -p veryslow --qp $1  -o genome.265 --no-wpp --no-deblock --no-sao --psy-rd 0 --tune psnr --psnr
ffmpeg -i genome.265 -y genome.yuv > /dev/null 2>&1
time ./decompress_hil.py 4096 4096 genome.yuv hilbert.csv
./compare.py tair8.txt decomp_a.txt
./compare.py tair9.txt decomp_b.txt

