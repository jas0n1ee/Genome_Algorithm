#!/usr/bin/env python
import math
import sys
import struct
import random
import json
alphabet = {'A':25, \
            'C':76, \
            'G':127,\
            'T':178,\
            'Z':229}
def write_yuv(genome_a, w, h, file_handle):
    for i in xrange(len(genome_a)):
        if genome_a[i] in alphabet:        
            t = struct.pack("B",alphabet[genome_a[i]])
            file_handle.write(t)        
        else:
            t = struct.pack("B",229)
            file_handle.write(t)        
    for i in xrange(w*h - len(genome_a)+w*h/2):
        t = struct.pack("B",229)
        file_handle.write(t)        

if __name__ == '__main__':
    with open("output.yuv","wb") as out:
        max_len = 0
        g_list = []
        for i in xrange(1,len(sys.argv)):
            with open(sys.argv[i],"r") as f:
                genome = ''
                next(f)
                for read in f:
                    if read[0] == '>':
                        break
                    genome +=read.rstrip()
            with open(sys.argv[i].split('.')[0]+'.txt',"w") as f:
                f.write(genome)
            g_list.append(genome)
            max_len = max(max_len, len(genome))
        block = math.ceil(max_len/64.0/64.0)
        w = int(math.ceil(math.sqrt(block))*64)
        h = w
        for i in xrange(len(sys.argv)-1):
            write_yuv(g_list[i],w,h,out)
        config={}
        config['size'] = [w,h]
        config['frame'] = len(sys.argv)-1
        config['name'] = sys.argv[1:]
        with open("config.json",'w') as c:
            c.write(json.dumps(config))
        print "Size: %dx%d; Frame:%d"%(w,h,len(sys.argv)-1)
        
