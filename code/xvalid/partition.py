lines = []
for line in open("train.btt.txt"):
    lines.append(line)
    
import sys
blocksize = len(lines) / int(sys.argv[2]) + 1

trainfile = open("train" + sys.argv[1] + ".txt", "w")
testfile = open("test" + sys.argv[1] + ".txt", "w")

block = 0
for i in range(len(lines)):
    if i > blocksize * (block + 1):
        block = block + 1
    
    if block == int(sys.argv[1]):
        testfile.write(lines[i].split("\t")[0] + "\t"
                     + lines[i].split("\t")[1] + "\n")
    else:
        trainfile.write(lines[i])
