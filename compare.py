#!/usr/bin/env python
def compare(filea,fileb)
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

