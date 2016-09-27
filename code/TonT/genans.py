# Read in te_crf and output answer to the screen

te_seg = open("te_seg", "r")
te_crf = open("te_crf", "r")


def getccnt(words, idx):
    ret = 0
    for i in range(0, idx+1):
        ret = ret + len(unicode(words[i], "utf-8"))
    return ret


for line in te_seg:
    words = line.strip("\n").split(" ")
    
    tags, probs = [], []

    for i in range(len(words)):
        tag, prob = te_crf.readline().strip("\n").split("\t")[1].split(":")
        prob = float(prob)

        tags.append(tag)
        probs.append(prob)
    
    te_crf.readline()

    if "RED" in tags:
        """
        st, end = -1, -1
        for i in range(len(tags)):
            if tags[i] == 'RED' and st == -1:
                st = i
            if tags[i] == 'RED':
                end = i

        print str(getccnt(words, st - 1)+1) + "\t" + str(getccnt(words, end))
        """
        
        idx = 0
        for i in range(len(probs)):
            if tags[i] == 'RED':
                idx = i
                
        for i in range(len(probs)):
            if tags[i] == 'RED' and probs[i] > probs[idx]:
                idx = i

        print str(getccnt(words, idx - 1)+1) + "\t" + str(getccnt(words, idx))
        
    else:
        idx = 0
        for i in range(len(probs)):
            if probs[i] < probs[idx]:
                idx = i
        
        print str(getccnt(words, idx - 1)+1) + "\t" + str(getccnt(words, idx))
