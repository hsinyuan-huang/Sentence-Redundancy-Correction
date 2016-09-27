import jieba
import jieba.posseg
def make_candidate(file_out, string, segs):
    for begin, end in segs:
        pattern = string[:begin]+string[end:]
        words = list(jieba.cut(pattern))
        file_out.write(' '.join(['%d-%d'%(begin+1, end), str(len(words))]+words)+'\n')
    file_out.write('--- 0\n')
