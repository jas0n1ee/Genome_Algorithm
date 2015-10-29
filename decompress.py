#!/usr/bin/env python
import math
import sys
import struct
import random
import json
alphabet = {25 :'A', \
            76 :'C', \
            127:'G',\
            178:'T',\
            229:'Z'}

def compare(filea,fileb):
    with open(filea,'r') as ori:
        with open(fileb,'r') as res:
            o = ori.read()
            r = res.read()
            diff = 0
            for i in xrange(min(len(o),len(r))):
                if not o[i]==r[i]:
                    if o[i] in ['A','T','C','G']:
                        diff += 1
            return diff*1.0/min(len(o),len(r))

def read_yuv(w,h,file_handle):
    genome = []
    f = file_handle
    for i in xrange(w*h):
        t = f.read(1)        
        r,=struct.unpack("B",t)
        genome.append(alphabet[int(math.floor(r/51.001)*51+25)])
    f.read(w*h/2)        
    return ''.join(genome)
if __name__ == '__main__':
    with open('config.json','r') as c:
        config = json.loads(c.read())
    frame_cnt = config['frame']
    f_name = config['name']
    size = config['size']
    with open('genome.yuv','rb') as stream:
        for i in xrange(frame_cnt):
            g_name = f_name[i].split('.')[0]
            with open('decomp_'+g_name+'.txt','w') as f:
                f.write(read_yuv(size[0],size[1],stream))
            print compare(g_name+'.txt','decomp_'+g_name+'.txt')

