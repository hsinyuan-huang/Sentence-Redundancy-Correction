#!/usr/bin/env python3
import sys

def grade(file_ans, file_res):
    total, t_recall, t_prec, match = 0, 0, 0, 0
    for ans, res in zip(file_ans.readlines(), file_res.readlines()):
        ind, origin, ansl, ansr = ans.split()
        if res.strip() == 'NULL':
            resl, resr = 1, 1
        else:
            resl, resr = res.split('-')
        (ansl, ansr, resl, resr) = map(int, (ansl, ansr, resl, resr))

        ints = max(0, min(ansr, resr)-max(ansl, resl)+1)
        total += 1
        t_recall += ints / (ansr-ansl+1)
        t_prec += ints / (max(ansr, resr)-min(ansl, resl)+1)
        if (ansl, ansr) == (resl, resr):
            match += 1
    recall = t_recall/total
    prec = t_prec/total
    print('ACC:', match/total)
    print('Recall:', recall)
    print('Prec:', prec)
    print('F1:', 2*recall*prec/(recall+prec))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: %s ANS YOUR_RESULT'%argv[0])
    file_ans  = open(sys.argv[1], 'r')
    file_res = open(sys.argv[2], 'r')
    grade(file_ans, file_res)
    file_ans.close()
    file_res.close()
