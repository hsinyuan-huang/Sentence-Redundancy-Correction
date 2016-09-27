#!/bin/bash

# Usage: ./solver.sh tr te out

python split.py $1 $2 # put in tr_txt, tr_val, te_txt, te_val

../stanford-segmenter/segment.sh -k ctb ./tr_txt UTF-8 0 > ./tr_seg
../stanford-segmenter/segment.sh -k ctb ./te_txt UTF-8 0 > ./te_seg

cd ../stanford-postagger
./stanford-postagger.sh ./models/chinese-distsim.tagger ../p2.train/te_seg > ../p2.train/te_pos
./stanford-postagger.sh ./models/chinese-distsim.tagger ../p2.train/tr_seg > ../p2.train/tr_pos

cd ../p2.train

# This method uses CRFsuite
python feat.py # create tr_feat & te_feat
crfsuite learn -mtr_model tr_feat
crfsuite tag -mtr_model -ri te_feat > te_crf
python genans.py > $3
# END

# This method uses LR with explicit poly2 hashing
#python feat.py # create tr_feat & te_feat
#python feat_svm.py # create tr_fsvm & te_fsvm from tr_feat & te_feat
#../liblinear/train -s 0 -c 0.5 -e 1e-6 tr_fsvm
#../libsvm/svm-train -c 0.12 -t 1 -g 1 -r 1 -d 2 -b 1 tr_fsvm
#../liblinear/predict -b 1 te_fsvm tr_fsvm.model te_svm
#../libsvm/svm-predict -b 1 te_fsvm tr_fsvm.model te_svm
#python genans_svm.py > $3
# END
