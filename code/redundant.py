#!/usr/bin/env python3
import sys

def convert(file_in, file_out):
    for line in file_in.readlines():
        ind, origin, begin, end = line.split()
        file_out.write(origin[int(begin)-1:int(end)]+'\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: %s INPUT OUTPUT'%argv[0])
    file_in = open(sys.argv[1], 'r')
    file_out = open(sys.argv[2], 'w')
    convert(file_in, file_out)
    file_in.close()
    file_out.close()
