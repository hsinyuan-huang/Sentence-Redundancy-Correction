te_svm = open("te_svm", "r")
te_seg = open("te_seg", "r")

te_svm.readline()

def getccnt(words, idx):
    ret = 0
    for i in range(0, idx+1):
        ret = ret + len(unicode(words[i], "utf-8"))
    return ret

for line in te_seg:
    words = line.strip("\n").split(" ")

    idx, minpb = 0, 2
    for i in range(len(words)):
        prob = te_svm.readline().strip("\n").split(" ")[1]
        prob = float(prob)

        if prob < minpb:
            idx, minpb = i, prob
    
    print str(getccnt(words, idx - 1)+1) + "\t" + str(getccnt(words, idx))
