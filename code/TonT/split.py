import sys

tr_txt = open("tr_txt", "w")
tr_val = open("tr_val", "w")
te_txt = open("te_txt", "w")
te_val = open("te_val", "w")

for line in open(sys.argv[1]):
    sent = line.strip("\n").split("\t")
    tr_txt.write(sent[1] + "\n")
    tr_val.write(sent[2] + "\t" + sent[3] + "\n")

for line in open(sys.argv[2]):
    te_txt.write(line.split("\t")[1])
    te_val.write("0\t0\n")
