tr_feat = open("tr_feat", "r")
te_feat = open("te_feat", "r")

tr_fsvm = open("tr_fsvm", "w")
te_fsvm = open("te_fsvm", "w")

feats = {}
feat_num = 10

for line in tr_feat:
    if line == "\n": continue

    for feat in line.strip("\n").split("\t")[1:]:
        if feat not in feats:
            feats[feat] = feat_num
            feat_num = feat_num + 1

for line in te_feat:
    if line == "\n": continue

    for feat in line.strip("\n").split("\t")[1:]:
        if feat not in feats:
            feats[feat] = feat_num
            feat_num = feat_num + 1

print feat_num

tr_feat = open("tr_feat", "r")
te_feat = open("te_feat", "r")

for line in tr_feat:
    if line == "\n": continue

    sent = line.strip("\n").split("\t")

    if sent[0] == "RED":
        tr_fsvm.write("1")
    else:
        tr_fsvm.write("0")
    
    inst = sorted([feats[x] for x in sent[1:]])

    for idx in inst:
        tr_fsvm.write(" " + str(idx) + ":1")
    
    tr_fsvm.write(" \n")
    
for line in te_feat:
    if line == "\n": continue

    sent = line.strip("\n").split("\t")

    if sent[0] == "RED":
        te_fsvm.write("1")
    else:
        te_fsvm.write("0")
   
    inst = sorted([feats[x] for x in sent[1:]])

    for idx in inst:
        te_fsvm.write(" " + str(idx) + ":1")

    te_fsvm.write(" \n")
