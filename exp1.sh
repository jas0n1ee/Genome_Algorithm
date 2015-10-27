#!/bin/bash
./compress_fasta.py tair8.fasta tair9.fasta
./x265_mod --input output.yuv --input-res 5568x5568 --fps 2 -p medium --qp $1  -o genome.265 --no-deblock --no-sao --psy-rd 0 --tune psnr --psnr
ffmpeg -i genome.265 -y genome.yuv
./decompress.py 5568 5568 genome.yuv
./compare.py tair8.txt decomp_a.txt
./compare.py tair9.txt decomp_b.txt

