# If the segment has cover with redundancy, I consider it as redundant

def createfeat(nme):
    segf = open(nme + "_seg", "r")
    posf = open(nme + "_pos", "r")
    ansf = open(nme + "_val", "r")

    outf = open(nme + "_feat", "w")

    while True:
        words = segf.readline().strip("\n").split(" ")
        pos_s = posf.readline().strip("\n").split(" ")

        if words == ['']: break

        pos_s = [x.split("#")[1] for x in pos_s]
    
        st, end = ansf.readline().strip("\n").split("\t")
        st, end = int(st), int(end)

        def cov(a, b, c, d):
            return max(a, c) <= min(b, d)

        def get(idx, seqs):
            if idx < 0: return "<s>"
            if idx >= len(seqs): return "<\s>"
            return seqs[idx]

        def sme(idx, idx2, seqs):
            if get(idx, seqs) == get(idx2, seqs): return "1"
            else: return "0"

        def smi(idx, idx2, seqs):
            flag = "0"
            for c in unicode(get(idx, seqs), "utf-8"):
                if c in unicode(get(idx2, seqs), "utf-8"): flag = "1"
            return flag

        ccnt = 0

        for i in range(len(words)):
            uniw = unicode(words[i], "utf-8")
            
            if cov(ccnt + 1, ccnt + len(uniw), st, end):
                outf.write("RED")
            else:
                #outf.write("O")
                outf.write(get(i, pos_s))

            if i == 0: outf.write("\t__BOS__")
            if i == len(words)-1: outf.write("\t__EOS__")

            for rp in range(-2, 3):
                outf.write(("\twrd[%d]=" % rp) + get(i + rp, words))
                outf.write(("\tpos[%d]=" % rp) + get(i + rp, pos_s))
                #outf.write(("\twsa[%d]=" % rp) + sme(i, i + rp, words))
                outf.write(("\tpsa[%d]=" % rp) + sme(i, i + rp, pos_s))
                outf.write(("\twsm[%d]=" % rp) + smi(i, i + rp, words))

            ccnt = ccnt + len(uniw)
            outf.write("\n")

        outf.write("\n")

createfeat("tr")
createfeat("te")
