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

label_index={}
with open('labellist_msn.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()

    for idx,line in enumerate(lines):
        line=line[:-1]
        label_index.setdefault(line, idx)

time_start = time.time()



raw_proj={}
with open("D:\\dataset\\MSN_NEWS\\raw\\category_raw_msn.tsv",'r',encoding='utf8') as f_r:
    i = 0
    while True:
        i += 1
        if not i % 10000:
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start = time_end
            print("iterrows:", i)
        line = f_r.readline()
        if not line:
            break
        lines = line.split('\t')
        url = lines[-1]
        url_pre = url.split('/')[4:-2]
        url = url.lower().split('/')[4:-2]
        for idx, i_url in enumerate(url):
            if len(i_url) > LEN_THRESH:
                continue
            i_url = i_url.replace('-', ' ').replace('_', ' ').replace('news', '').replace('more', '').replace('videos',"").replace("video", '')
            i_url = i_url.strip()
            i_url = wnl.lemmatize(i_url, 'n')
            if len(i_url) < 2:
                continue
            if i_url in label_proj.keys():
                i_url = label_proj[i_url]
            if i_url in label_index.keys():
                raw_proj.setdefault(url_pre[idx], i_url)



with open('raw_projction.txt','w+',encoding='utf8') as f_w:
    for key in raw_proj.keys():
        f_w.write(key+"\t"+raw_proj[key]+'\n')
