# encoding: utf-8
out = open("train.btt.txt", "w")


# random shuffle
lines = []
for line in open("p2.train.txt", "r"):
    lines.append(line)

import random
random.shuffle(lines)

# change form
redun_len = {}

for line in lines:
    linels = line.strip("\n").split("\t")
    sent1 = unicode(linels[1], "utf-8")
    sent2 = unicode(linels[2], "utf-8")

    ansi, ansj = -1, -1

    for i in range(len(sent1)):
        for j in range(i + 1, len(sent1)+1):
            if sent2 == sent1[:i] + sent1[j:]:
                ansi = i + 1
                ansj = j
                
                redun_len[ansj - ansi] = redun_len.setdefault(ansj - ansi, 0) + 1
    
    out.write(linels[0] + "\t" + linels[1] + "\t" + str(ansi) + "\t" + str(ansj) + "\n")

print redun_len
