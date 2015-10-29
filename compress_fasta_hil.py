#!/usr/bin/env python
import math
import sys
import struct
import random
alphabet = {'A':25, \
            'C':76, \
            'G':127,\
            'T':178,\
            'Z':229}
def write_yuv(genome_a, genome_b, hil, filename = 'output.yuv'):
    length = max(len(genome_a), len(genome_b))
    if length < len(hil):
        print"Error hilbert curve length not enough"
        return
    cnt_a = 0
    cnt_b = 0
    w = int(math.sqrt(len(hil)))
    h = w
    m_a = [0]*w*h
    m_b = [0]*w*h
    for i in xrange(len(hil)):
        if genome_a[i] in alphabet:
            m_a[hil[i]-1] = genome_a[i]
        else: 
            m_a[hil[i]-1] = 'Z'
            cnt_a +=1
        if genome_b[i] in alphabet:
            m_b[hil[i]-1] = genome_b[i]
        else: 
            m_b[hil[i]-1] = 'Z'
            cnt_b +=1
    with open(filename,"wb") as f:
        for i in xrange(w*h):
            t = struct.pack("B",alphabet[m_a[i]])
            f.write(t)        
        for i in xrange(w*h/2):
            t = struct.pack("B",229)
            f.write(t)        
        for i in xrange(w*h):
            t = struct.pack("B",alphabet[m_b[i]])
            f.write(t)        
        for i in xrange(w*h/2):
            t = struct.pack("B",229)
            f.write(t)        
    print "Total: %f and %f percent of content out of dictionary"%(cnt_a*100.0/w/h,cnt_b*100.0/w/h)
    print "x265 --input %s --input-res %dx%d --fps 2 -p medium -q 22 -o genome.265 --psy-rd 0 --tune psnr --psnr"%(filename,w,h)
    print "ffmpeg -i genome.265 -y genome.yuv"
    print "python decompress.py %d %d genome.yuv"%(w,h)
    return w, h
if __name__ == '__main__':
    file_a = sys.argv[1]
    file_b = sys.argv[2]
    hil = sys.argv[3]
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
    with open(hil,"r") as f:
        m_hil = [];
        for line in f:
            m_hil.append(int(float(line)))
    print len(m_hil)
    write_yuv(genome_a, genome_b, m_hil)
