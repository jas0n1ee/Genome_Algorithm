#!/usr/bin/env python
import math
import sys
import struct
import random
"""
alphabet = {0  :'A',\
            8  :'A',\
            24 :'C',\
            40 :'G',\
            56 :'T',\
            72 :'U',\
            88 :'R',\
            104:'Y',\
            120:'K',\
            136:'M',\
            152:'S',\
            168:'W',\
            184:'B',\
            200:'D',\
            216:'H',\
            232:'V',\
            248:'N'}
"""
alphabet = {25 :'A', \
            76 :'C', \
            127:'G',\
            178:'T',\
            229:'Z'}

def read_yuv(w,h,filename = 'output.yuv'):
    genome_a = [];
    genome_b = [];
    with open(filename,"rb") as f:
        for i in xrange(w*h):
            t = f.read(1)        
            r,=struct.unpack("B",t)
            genome_a.append(alphabet[int(math.floor(r/51.001)*51+25)])
        f.read(w*h/2)        
        for i in xrange(w*h):
            t = f.read(1)        
            r,=struct.unpack("B",t)
            genome_b.append(alphabet[int(math.floor(r/51.001)*51+25)])
        f.read(w*h/2)        
    return genome_a, genome_b
if __name__ == '__main__':
    w = int(sys.argv[1])
    h = int(sys.argv[2])
    genome_a, genome_b = read_yuv(w, h, sys.argv[3])
    with open('decomp_a.txt',"w") as f:
        f.write(''.join(genome_a))
    with open('decomp_b.txt',"w") as f:
        f.write(''.join(genome_b))
