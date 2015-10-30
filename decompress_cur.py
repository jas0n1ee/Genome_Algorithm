#!/usr/bin/env python
import math
import sys
import struct
import random
alphabet = {25 :'A', \
            76 :'C', \
            127:'G',\
            178:'T',\
            229:'Z'}

def read_yuv(w,h,filename,hil):
    with open(hil,"r") as f:
        m_hil = []
        for line in f:
            m_hil.append(int(float(line)))
    genome_a = [0]*len(m_hil)
    genome_b = [0]*len(m_hil)
    temp_a = []
    temp_b = []
    with open(filename,"rb") as f:
        for i in xrange(w*h):
            t = f.read(1)        
            r,=struct.unpack("B",t)
            temp_a.append(alphabet[int(math.floor(r/51.001)*51+25)])
        f.read(w*h/2)        
        for i in xrange(w*h):
            t = f.read(1)        
            r,=struct.unpack("B",t)
            temp_b.append(alphabet[int(math.floor(r/51.001)*51+25)])
        f.read(w*h/2)        
    for i in xrange(len(m_hil)):
        genome_a[i] = temp_a[m_hil[i]-1]
        genome_b[i] = temp_b[m_hil[i]-1]
    return genome_a, genome_b
if __name__ == '__main__':
    w = int(sys.argv[1])
    h = int(sys.argv[2])
    cur = sys.argv[4]
    genome_a, genome_b = read_yuv(w, h, sys.argv[3], cur)
    with open('decomp_a.txt',"w") as f:
        f.write(''.join(genome_a))
    with open('decomp_b.txt',"w") as f:
        f.write(''.join(genome_b))
