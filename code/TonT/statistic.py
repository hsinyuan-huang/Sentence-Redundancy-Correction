#encoding: utf-8

uni = 0
bi = 0
one = 0
oneuni = 0

sm1 = 0
sm2 = 0

tot = 0

def myseg(x, y, sent):
    bg = 0
    ed = 0

    cnt = 0
    for i in range(len(sent)):
        if i == x: bg = cnt + 1
        cnt = cnt + len(sent[i])
        if i == y: ed = cnt
    
    return (bg, ed)

ans = open("tr_val", "r")
for line in open("tr_seg", "r"):
    st, end = ans.readline().strip("\n").split("\t")
    st, end = int(st), int(end)
    
    sent = unicode(line, "utf-8").strip("\n").split(" ")

    tot = tot + 1   

    unif, bif, sm1f, sm2f, onef = 0, 0, 0, 0, 0

    if end - st == 0: onef = 1

    for i in range(len(sent)):
        if myseg(i, i, sent) == (st, end):
            unif = 1
        if  myseg(i, i, sent)[0] <= st and myseg(i, i, sent)[1] >= end:
            sm1f = 1
        if i < len(sent) - 1 and myseg(i, i+1, sent) == (st, end):
            bif = 1 
        if i < len(sent) - 1 and\
            myseg(i, i+1, sent)[0] <= st and myseg(i, i+1, sent)[1] >= end:
            sm2f = 1

    uni = uni + unif
    bi = bi + bif
    sm1 = sm1 + sm1f
    sm2 = sm2 + sm2f
    one = one + onef

    oneuni = oneuni + (onef or unif)

print str(1. * uni / tot) + "% of redun is exactly 1 segmented chunk"
print str(1. * sm1 / tot) + "% of redun is smaller or equal to 1 segmented chunk"
print str(1. * bi / tot) + "% of redun is exactly 2 segmented chunk"
print str(1. * sm2 / tot) + "% of redun is smaller or equal to 2 segmented chunk"
