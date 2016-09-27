import sys
ans = open(sys.argv[1], "r")
val = open(sys.argv[2], "r")

linecnt = 0
ave_rec = 0
ave_pre = 0
tot_acc = 0

for line in ans:
    st, end = val.readline().strip("\n").split("\t")
    A, B, ans_st, ans_end = line.strip("\n").split("\t")

    st, end = int(st), int(end)
    ans_st, ans_end = int(ans_st), int(ans_end)
    
    linecnt = linecnt + 1

    def cov(a, b, c, d):
        if min(b, d) - max(a, c) >= 0:
            return min(b, d) - max(a, c) + 1
        else: return 0

    rec = cov(st, end, ans_st, ans_end) * 1. / (ans_end - ans_st + 1)
    pre = cov(st, end, ans_st, ans_end) * 1. / (end - st + 1)

    ave_rec = ave_rec + rec
    ave_pre = ave_pre + pre

    if rec == 1 and pre == 1:
        tot_acc = tot_acc + 1

ave_rec = 1. * ave_rec / linecnt
ave_pre = 1. * ave_pre / linecnt
tot_acc = 1. * tot_acc / linecnt

print "accuracy: " + str(tot_acc)
print "ave. precision: " + str(ave_pre)
print "ave. recall: " + str(ave_rec)
print "F1-scores: " + str(2. * (ave_pre * ave_rec) / (ave_pre + ave_rec))
