
import time

import pandas as pd
import numpy as np
import os
import re
print('Repeated "title+body" paper merge......')
#"C:\\Users\\t-yunche\\file\\example1.tsv"
# data=pd.read_csv("C:\\Users\\t-yunche\\file\\dataset\\Flipboard_Join_Body.tsv",sep='\t',error_bad_lines=False,encoding='utf8',header=None)
with open("C:\\Users\\t-yunche\\file\\dataset\\Flipboard_Join_Body.tsv",'r',encoding='utf8') as f_r:
    with open("FJB_Merge.tsv",'w+',encoding='utf8') as f_w:
        merge=f_r.readline()
        merge=merge.split('\t')
        pre=merge
        i=0
        time_start = time.time()

        while(True):
            i+=1
            if (i % 50000 == 0):
                # break
                if(i==50000):
                    time_end = time.time()
                    print('50000 data nodes\' time cost', time_end - time_start, 's')
                    time_start = time_end
                print("iterrows:", i)
            cur=f_r.readline()
            if not cur:
                break
            cur=cur.split('\t')
            if cur.__len__()!=4:
                continue

            if cur[0]==pre[0] or cur[1]==pre[1] :
                t_l=cur[2].split(', ')
                for t in t_l:
                    if t not in merge[2].split(', '):
                        merge[2]+=', '+t
            else:
                f_w.write('\t'.join(merge[:-1])+'\n')
                merge=cur
            pre=cur

        f_w.write('\t'.join(merge[:-1]) + '\n')

