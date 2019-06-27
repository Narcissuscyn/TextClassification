from nltk.corpus import wordnet as wn

import nltk
from nltk import*
import enchant
import time

from enchant.checker import SpellChecker

from nltk.stem import WordNetLemmatizer
import json
import re


wnl = WordNetLemmatizer()

st = LancasterStemmer()
LEN_THRESH=20
dict_wrong={}
label_proj={}
with open('../tools/my_words.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for line in lines:
        line=line[:-1].split(',')
        label_proj[line[0]]=line[1]
with open('../tools/wrong_list.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for l in lines:
        dict_wrong[l[:-1]]=1


label_dict={}
time_start = time.time()
label_son={}
with open("D:\\dataset\\MSN_NEWS\\raw\\category_raw_msn.tsv",'r',encoding='utf8') as f_r:
    with open('D:\\dataset\\MSN_NEWS\\raw\\category_label_msn.tsv','w+',encoding='utf8') as f_w:
        i=0
        while True:
            i+=1
            if not i%10000:
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                time_start = time_end
                print("iterrows:", i)
            line=f_r.readline()
            if not line:
                break
            lines=line.split('\t')
            url=lines[-1]
            url=url.lower().split('/')[4:-2]
            label_str = []
            for i_url in url:
                if len(i_url)>LEN_THRESH:
                    continue
                i_url=i_url.replace('-',' ').replace('_',' ').replace('news','').replace('more','').replace('videos',"").replace("video",'')
                i_url=i_url.strip()
                i_url = wnl.lemmatize(i_url, 'n')
                if len(i_url)<2 or i_url in dict_wrong.keys() or i_url in label_str:
                    continue
                if i_url in label_proj.keys():
                    # print(i_url)
                    i_url = label_proj[i_url]
                label_dict.setdefault(i_url, 0)
                if i_url not in label_str:
                    label_str.append(i_url)
                    label_dict[i_url]+=1
            if label_str==[]:
                continue

            if len(label_str)>0:
                label_son.setdefault(label_str[0], [])
                for l in label_str[1:]:
                    if l not in label_son[label_str[0]]:
                        label_son[label_str[0]].append(l)
            lines[-1]=lines[-1][:-1]
            lines.append(','.join(label_str))
            f_w.write('\t'.join(lines)+'\n')


with open('labellist_msn_raw.txt','w+',encoding='utf8') as f_w:
    for key in label_dict.keys():
        f_w.write(key+'\n')


print(label_son)
with open('labeltree_son.json', 'w+') as fp:
  json.dump(label_son, fp)
