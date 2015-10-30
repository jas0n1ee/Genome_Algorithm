#!/bin/bash
qp=$1
preset=medium
./compress_fasta.py tair8.fasta tair9.fasta
./x265_mod --input output.yuv --input-res 5568x5568 --fps 1 -p $preset --qp $qp  -o genome_${qp}.265 --no-wpp --no-deblock --no-sao --psy-rd 0 --tune psnr --psnr 2>&1|grep "PSNR" >./log/265log_${qp}
ffmpeg -i genome_${qp}.265 -y genome.yuv
./decompress.py > ./log/qp${qp}_err_rate

