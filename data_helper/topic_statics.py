import pandas as pd
from collections import OrderedDict
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

print("loading dataset...")
data=pd.read_csv("C:\\Users\\t-yunche\\file\\dataset\\Flipboard_Join_Body.tsv",sep='\t',error_bad_lines=False,encoding='utf8',header=None)

freq={}
freq_thresh=10
rule=re.compile(u"[^a-zA-Z ]")

print("data count:",data.shape[0])
for i,d in enumerate(data.iterrows()):
    arr=d[1].array
    if (arr.shape[0] != 4 or arr[-2]is np.nan):
        # print(d)
        continue
    topic = arr[-2]
    topic = topic.lower()
    topic = topic.split(', ')
    for a in topic:
        a = rule.sub("", a)
        if (a == ''):
            continue
        if(' ' not in a):
            a = wnl.lemmatize(a)  # lemmatization
        if a not in freq.keys():
            freq[a]=0
        freq[a]+=1

print("move before: ",freq.__len__())
keys=list(freq.keys())
for key in keys:
    if(freq[key]<freq_thresh):
        freq.pop(key)
print("move after: ",freq.__len__())

freq = sorted(freq.items(), key=lambda x: x[1],reverse=True)
print(freq)


f=open("./label1.txt",'w+',encoding='utf-8')
for idx,item in enumerate(freq):
    print(item)
    f.write((item[0]+'\n'))
f.close()