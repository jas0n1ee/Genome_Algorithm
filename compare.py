#!/usr/bin/env python
import sys
with open(sys.argv[1],'r') as ori:
    with open(sys.argv[2],'r') as res:
        o = ori.read()
        r = res.read()
        diff = 0
        for i in xrange(min(len(o),len(r))):
            if not o[i]==r[i]:
                if o[i] in ['A','T','C','G']:
                    diff += 1
                    print o[i], r[i]
        print diff*1.0/min(len(o),len(r))
