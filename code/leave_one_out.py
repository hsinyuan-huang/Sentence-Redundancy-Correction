#!/usr/bin/env python3
import sys
import candidate

def process(file_in, file_out):
    for line in file_in.readlines():
        ind, origin, begin, end = line.split()
        segs = []
        for i in range(len(origin)):
            segs.append((i, i+1))
        candidate.make_candidate(file_out, origin, segs)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: %s INPUT OUTPUT'%sys.argv[0])
    file_in = open(sys.argv[1], 'r')
    file_out = open(sys.argv[2], 'w')
    process(file_in, file_out)
    file_in.close()
    file_out.close()
