#!/usr/bin/env python3
import sys

def convert(file_in, file_out):
    for line in file_in.readlines():
        ind, origin, correct = line.split()
        origin += '\0'
        correct += '\0'
        begin, end = 0, 0
        for i in range(len(origin)):
            if origin[i] != correct[i]:
                begin = i
                break
        for i in range(begin, len(origin)-1):
            if origin[i+1:] == correct[begin:]:
                end = i
                break
        file_out.write('%s %s %d %d\n'%(ind, origin[:-1], begin+1, end+1))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: %s INPUT OUTPUT'%argv[0])
    file_in = open(sys.argv[1], 'r')
    file_out = open(sys.argv[2], 'w')
    convert(file_in, file_out)
    file_in.close()
    file_out.close()
