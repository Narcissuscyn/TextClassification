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

def full_to_splits(root, file, max_cnt):
    '''

    :param root:source and target file directory
    :param file:source file name
    :param max_cnt:max data counts each data split
    :return:None
    '''
    cur_cnt = 0
    dir_idx = 1
    if not os.path.exists(root):
        os.mkdir(root)
    f = open(os.path.join(root, str(dir_idx) + ".tsv"), 'w+', encoding='utf8')
    time_start = time.time()
    with open(file, 'r', encoding='utf8') as f_r:
        i = -1
        while True:
            i += 1
            data_i = f_r.readline()
            if not data_i:
                break
            if (i % 10000 == 0):
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                time_start = time_end
                print("iterrows:", i)
            if (cur_cnt == max_cnt):
                print(i)
                dir_idx += 1
                f.close()
                f = open(os.path.join(root, str(dir_idx) + ".tsv"), 'w+', encoding='utf8')
                cur_cnt = 0
            f.write(data_i)
            cur_cnt += 1
    f.close


def full_to_tst_trn(root,sou_file,num_label=154):
    '''
    this function is for divide feature dataset into test split and train split.
    :param root:feature file directory
    :param sou_file:feature file name
    :param num_label:topic counts
    :return:
    '''
    print("loading data...")
    data = pd.read_csv(os.path.join(root, sou_file), sep='\t', error_bad_lines=False, encoding='utf8',
                       header=None, skiprows=1)  # skiprows:skip 1 row from top
    print("data.shape:",data.shape)
    print("spliting test and train file...")
    f1 = open(os.path.join(root, 'trn_X_Xf.txt'), 'w+', encoding='utf8')
    f2 = open(os.path.join(root, 'trn_X_Y.txt'), 'w+', encoding='utf8')
    num_trn = int(data.shape[0] * 0.8)
    num_tst = data.shape[0] - num_trn
    # num_label = 6000
    # num_ft=2653075
    # num_ft=2524528
    # num_ft = 198169
    num_ft=167697
    f1.write(str(num_trn) + ' ' + str(num_ft) + '\n')
    f2.write(str(num_trn) + ' ' + str(num_label) + '\n')
    isTest = False
    time_start = time.time()
    print("total data count:", data.shape[0])
    train_cnt = 0
    for i, r in enumerate(data.iterrows()):
        if (i % 50000 == 0):
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start = time_end
            print("iterrows:", i)

        if (not isTest and i == num_trn):
            train_cnt = i
            print("train data count:", i)
            f1 = open(os.path.join(root, 'tst_X_Xf.txt'), 'w+', encoding='utf8')
            f2 = open(os.path.join(root, 'tst_X_Y.txt'), 'w+', encoding='utf8')
            f1.write(str(num_tst) + ' ' + str(num_ft) + '\n')
            f2.write(str(num_tst) + ' ' + str(num_label) + '\n')
            isTest = True
        labels = r[1][0][:r[1][0].find(' ')].split(',')
        fts = r[1][0][r[1][0].find(' ') + 1:]
        labels_r = ""
        for id, l in enumerate(labels):
            if (id != len(labels) - 1):
                labels_r += l + ':1 '
            else:
                labels_r += l + ':1\n'
        f2.write(labels_r)
        f1.write(fts + '\n')
    print("test data count:", i - train_cnt + 1)
    f1.close()
    f2.close()


if __name__=="__main__":
    # tar_dir = "D:\\dataset\\MSN_NEWS\\annotated"
    # full_to_splits(tar_dir,os.path.join(tar_dir,"news_msn.tsv"),370000)
    full_to_tst_trn("D:\\dataset\\MSN_NEWS\\ft","msn_x_y.txt",154)