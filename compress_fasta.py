#!/usr/bin/env python
import math
import sys
import struct
import random
alphabet = {'A':8, \
            'C':24, \
            'G':40, \
            'T':56, \
            'U':72, \
            'R':88, \
            'Y':104,\
            'K':120,\
            'M':136,\
            'S':152,\
            'W':168,\
            'B':184,\
            'D':200,\
            'H':216,\
            'V':232,\
            'N':248}



def write_yuv(genome_a, genome_b, filename = 'output.yuv'):
    length = max(len(genome_a), len(genome_b))
    block = math.ceil(length/64.0/64.0)
    w = int(math.ceil(math.sqrt(block))*64)
    h = w
    if w*h < length:
        print "error length"
        return 
    with open(filename,"wb") as f:
        for i in xrange(len(genome_a)):
            t = struct.pack("B",alphabet[genome_a[i]])
            f.write(t)        
        for i in xrange(w*h - len(genome_a)+w*h/2):
            t = struct.pack("B",248)
            f.write(t)        
        for i in xrange(len(genome_b)):
            t = struct.pack("B",alphabet[genome_b[i]])
            f.write(t)        
        for i in xrange(w*h - len(genome_b)+w*h/2):
            t = struct.pack("B",248)
            f.write(t)  
    print "x265 --input %s --input-res %dx%d --fps 2 -p medium -q 22 -o genome.265 --psy-rd 0 --tune psnr --psnr"%(filename,w,h)
    print "ffmpeg -i %s -y genome.yuv"%(filename)
    print "python decompress.py %d %d genome.yuv"%(w,h)
    return w, h
if __name__ == '__main__':
    file_a = sys.argv[1]
    file_b = sys.argv[2]
    with open(file_a,"r") as f:
        genome_a = ''
        next(f)
        for read in f:
            if read[0] == '>':
                break
            genome_a +=read.rstrip()
    with open(file_a.split('.')[0]+'.txt',"w") as f:
        f.write(genome_a)
    with open(file_b,"r") as f:
        genome_b = ''
        next(f)
        for read in f:
            if read[0] == '>':
                break
            genome_b += read.rstrip()
    with open(file_b.split('.')[0]+'.txt',"w") as f:
        f.write(genome_b)
    write_yuv(genome_a, genome_b)
