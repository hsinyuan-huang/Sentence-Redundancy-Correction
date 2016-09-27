#!/usr/bin/env python3
import sys
import candidate

def process(file_in, file_out, reds):
    for line in file_in.readlines():
        ind, origin, begin, end = line.split()
        segs = []
        for i in range(len(origin)):
            if origin[i] in reds:
                segs.append((i, i+1))
        candidate.make_candidate(file_out, origin, segs)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('usage: %s INPUT OUTPUT REDUNDENT'%sys.argv[0])
    file_in = open(sys.argv[1], 'r')
    file_out = open(sys.argv[2], 'w')
    file_red = open(sys.argv[3], 'r')
    
    reds = set()
    for word in file_red.readlines():
        word = word.strip()
        if len(word) == 1:
            print(word)
            reds.add(word)
    process(file_in, file_out, reds)
    file_in.close()
    file_out.close()
