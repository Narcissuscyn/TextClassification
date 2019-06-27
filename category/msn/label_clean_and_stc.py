'''

@ description:
    this is a python script for evaluating label distribution, i.e. multi-label frequency distribution
@auther by Narcissus
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

print("loading dataset...")

label_proj={}
with open('../tools/my_words.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for line in lines:
        line=line[:-1].split(',')
        label_proj.setdefault(line[0],line[1])

label_list={}
with open('../msn/labellist_msn.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for line in lines:
        line=line[:-1]
        if line in label_proj.keys():
            line=label_proj[line]
        label_list.setdefault(line,line)
dict_wrong={}
with open('../tools/wrong_list.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for l in lines:
        dict_wrong[l[:-1]]=1



data_dir='D:\\dataset\\MSN_NEWS\\raw'
data_freq={}
with open(os.path.join(data_dir,"category_label_msn.tsv"),'r',encoding='utf8')as f_r:
    with open(os.path.join(data_dir,"category_label_msn_clean.tsv"),'w+',encoding='utf8')as f_w:
        i=0
        while True:
            line=f_r.readline()
            if not line:
                break
            if i%10000==0:
                print('line ',i)
            i+=1
            line=line.split('\t')
            tar_label=[]
            labels=line[-1][:-1].split(',')
            for l in labels:
                if l in dict_wrong.keys():
                    continue
                if l in label_proj.keys():
                    # print(l)
                    l=label_proj[l]
                if l in label_list.keys():
                    data_freq.setdefault(l,0)
                    if l not in tar_label:
                        data_freq[l]+=1
            #             tar_label.append(l)
            # if len(tar_label)!=0:
            #     line[-1]=','.join(tar_label)
            #     f_w.write('\t'.join(line)+'\n')
print("writing data...")

data_freq = sorted(data_freq.items(), key=lambda x: x[1],reverse=True)

FREQ_THRESH=0
with open('../msn/data_freq.txt','w+',encoding='utf8')as f_w:
    print(data_freq)
    for item in data_freq:
        if(item[1]>FREQ_THRESH):
            f_w.write(item[0]+" "+str(item[1])+'\n')


data_values=[data[1] for data in data_freq]
max_len=100
x=list(range(0,max_len))

print("drawing figure...")
fig=plt.figure()
plt.bar(x,data_values[:max_len],color="blue")

plt.xlabel("labbel-num")
plt.ylabel("label-freq")
plt.title("label statistic")
plt.savefig("../msn/fig_label_freq.jpg")
plt.show()
