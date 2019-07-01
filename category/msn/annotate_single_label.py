import json
import sys
import os
import time
label_father={}
with open('./labeltree_father.json', 'r', encoding='utf8') as f_r:
    label_father = json.load(f_r)

label_index={}
with open('label_index_msn.json', 'r', encoding='utf8') as f_r:
    label_index = json.load(f_r)
DATA_DIR="D:\\dataset\\MSN_NEWS"
if not os.path.exists(os.path.join(DATA_DIR,"annotated")):
    os.mkdir(os.path.join(DATA_DIR,"annotated"))
label_proj={}
with open('../tools/my_words.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for line in lines:
        line=line[:-1].split(',')
        label_proj.setdefault(line[0],line[1])
# with open(os.path.join(DATA_DIR,"raw", str(sys.args[1])+".tsv"),'r',encoding='utf8') as f_r:
#     with open(os.path.join(DATA_DIR,"annotated", str(sys.args[1])+".tsv"),'w+',encoding='utf8') as f_w:

with open(os.path.join(DATA_DIR, "raw", "category_label_msn.tsv"), 'r', encoding='utf8') as f_r:
    with open(os.path.join(DATA_DIR,"annotated","category_msn.tsv"),'w+',encoding='utf8') as f_w:
        i=0
        time_start = time.time()
        while True:
            line=f_r.readline()
            if not line:
                break
            i+=1
            if not i%10000:
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                time_start = time_end
                print("iterrows:", i)
            line=line.split('\t')
            tags=line[-1][:-1]
            labels=[]
            labels_idxes=[]
            tags=tags.split(',')
            for tag in tags:
                if tag in label_proj.keys():
                    tag=label_proj[tag]
                if tag in label_index.keys():
                    labels.append(tag)
                    labels_idxes.append(str(label_index[tag]))
                    if tag in label_father.keys():
                        for l_f in label_father[tag]:
                            if l_f not in labels:
                                labels.append(l_f)
                                labels_idxes.append(str(label_index[l_f]))

            if len(labels)==0:
                continue
            line[-1]=','.join(labels)
            line.append(','.join(labels_idxes))
            f_w.write('\t'.join(line)+'\n')
