#!/bin/bash
preset=medium
time ./compress_fasta_cur.py tair8.fasta tair9.fasta $2
./x265_mod --input output.yuv --input-res 4096x4096 --fps 1 -p $preset --qp $1 -s 32 --max-tu-size 8 -o genome_${1}.265 --no-wpp --no-deblock --no-sao --psy-rd 0 --tune psnr --psnr > ./log/265log_qp$1 2>&1
ffmpeg -i genome_${1}.265 -y genome.yuv > /dev/null 2>&1
time ./decompress_cur.py 4096 4096 genome.yuv $2
./compare.py tair8.txt decomp_a.txt
./compare.py tair9.txt decomp_b.txt
