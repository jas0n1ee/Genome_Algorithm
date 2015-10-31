#!/usr/bin/env python
import random
import sys


def gen_genome(length):
    genome=[]
    for i in xrange(length):
        if random.random()<0.99:
            genome.append(random.choice(['A','T','C','G']))
        else:
            genome.append('N')
    return genome

def insertion(genome,rate):
    cnt = 0
    for i in xrange(len(genome)):
        if random.random()<rate:
            if random.random()<0.99:
                genome.insert(i,random.choice(['A','T','C','G']))
            else:
                genome.insert(i,'N')
            cnt += 1
    print "insertion num %d/ insertion rate %f\n"%(cnt, cnt*1.0/len(genome))
    return genome

def variation(genome, rate):
    for i in xrange(len(genome)):
        if random.random()<rate*4/3.0:
            genome[i] = random.choice(['A','T','C','G'])

    return genome

if __name__ == '__main__':
    genome = gen_genome(int(sys.argv[1]))
    with open('text1.fasta','w') as f:
        f.write('>THIS IS A TEST FASTA FILE\n')
        f.write(''.join(genome))
    genome = variation(genome,0.01)
    genome = insertion(genome,0.000002)
    with open('text2.fasta','w') as f:
        f.write('>THIS IS A TEST FASTA FILE\n')
        f.write(''.join(genome))
