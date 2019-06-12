# import time
#
# import pandas as pd
# import numpy as np
# import os
# import re
# # data=pd.read_csv("C:\\Users\\t-yunche\\file\\dataset\\Flipboard_Join_Body.tsv",sep='\t',error_bad_lines=False,encoding='utf8',header=None)
#
#
# COUNT=240000
# num=0
# #8-splits
# dir_idx=1
#
# DATA="C:\\Users\\t-yunche\\file\dataset\\topic_clean"
# if not os.path.exists(DATA):
#     os.mkdir(DATA)
#
# f=open(os.path.join(DATA, str(dir_idx)+".tsv"),'w+',encoding='utf8')
# time_start = time.time()
# invalid_cnt=0
# rule=re.compile(u"[^a-zA-Z ]")
# rule1=re.compile(u"[^a-zA-Z ,]")
#
# with open('C:\\Users\\t-yunche\\file\\code\\data_helper\\res\\FJB_Merge_remove_shuffle.tsv','r',encoding='utf8') as f_r:
#     i=-1
#     while True:
#         i+=1
#         d=f_r.readline()
#         if(i%10000==0):
#             time_end = time.time()
#             print('time cost', time_end - time_start, 's')
#             time_start=time_end
#             print("iterrows:",i)
#         data_i=d[1].array
#         # if (data_i.shape[0] != 4 or data_i[-2]==np.nan):
#         #     print("invalid text: ",data_i)
#         #     invalid_cnt+=1
#         #     continue
#         if(num==COUNT):
#             print(i)
#             dir_idx+=1
#             f.close()
#             f=open(os.path.join(DATA, str(dir_idx)+".tsv"),'w+',encoding='utf8')
#             num=0
#         f.write(rule.sub("", data_i[0]).lower())
#         f.write('\t')
#         f.write(rule.sub("", data_i[1]).lower())
#         f.write('\t')
#         f.write(rule1.sub("", str(data_i[2])).lower())
#         f.write('\n')
#         num+=1
#
#     f.close()
#
# print("invalid_cnt: ",invalid_cnt)
#


import time

import pandas as pd
import numpy as np
import os
import re
# data=pd.read_csv("C:\\Users\\t-yunche\\file\\dataset\\Flipboard_Join_Body.tsv",sep='\t',error_bad_lines=False,encoding='utf8',header=None)


COUNT=240000
num=0
#8-splits
dir_idx=1

DATA="C:\\Users\\t-yunche\\file\dataset\\topic_clean"
if not os.path.exists(DATA):
    os.mkdir(DATA)

f=open(os.path.join(DATA, str(dir_idx)+".tsv"),'w+',encoding='utf8')
time_start = time.time()
with open('./res/FJB_Merge_remove_shuffle.tsv','r',encoding='utf8') as f_r:
    i=-1
    while True:
        i+=1
        data_i=f_r.readline()
        if not data_i:
            break
        if(i%10000==0):
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start=time_end
            print("iterrows:",i)
        if(num==COUNT):
            print(i)
            dir_idx+=1
            f.close()
            f=open(os.path.join(DATA, str(dir_idx)+".tsv"),'w+',encoding='utf8')
            num=0
        f.write(data_i)
        num+=1

f.close
