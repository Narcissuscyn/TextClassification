import pandas as pd
from collections import OrderedDict
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
import os
print("loading dataset...")
# data=pd.read_csv("C:\\Users\\t-yunche\\file\\dataset\\Flipboard_Join_Body.tsv",sep='\t',error_bad_lines=False,encoding='utf8',header=None)
data_dir="C:\\Users\\t-yunche\\file\\dataset\\topic\\source"
label_list=[]
i=1
while(i<7):
    file=os.path.join(data_dir,str(i)+'.tsv')
    print("loading file ", file)
    data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
    label_list.extend(data[2])
    del data
    i+=1


freq={}
freq_thresh=10
rule=re.compile(u"[^a-zA-Z ]")

# print("data count:",data.shape[0])
for i,d in enumerate(label_list):

    topic = d.split(', ')
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


f=open("./label_th10.txt",'w+',encoding='utf-8')
for idx,item in enumerate(freq):
    print(item)
    f.write((item[0]+'\n'))
f.close()