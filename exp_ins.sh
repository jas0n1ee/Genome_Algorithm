#!/bin/bash
preset=medium
qp=$3
time ./compress_fasta_cur.py $1 $2 $4
./x265_mod --input output.yuv --input-res 1024x1024 --fps 1 -p $preset --qp $qp -s 32 --max-tu-size 8 -o genome_${qp}.265 --no-wpp --no-deblock --no-sao --psy-rd 0 --tune psnr --psnr > ./log/265log_qp$1 2>&1
ffmpeg -i genome_${qp}.265 -y genome.yuv > /dev/null 2>&1
time ./decompress_cur.py 1024 1024 genome.yuv $4
./compare.py ${1%%.*}.txt decomp_a.txt
./compare.py ${2%%.*}.txt decomp_b.txt
