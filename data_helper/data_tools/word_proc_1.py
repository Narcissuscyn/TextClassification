

import pandas as pd
import re
import sys
from nltk.stem import WordNetLemmatizer
import time
import os
wnl = WordNetLemmatizer()
'''
get stop words list
'''
print('loading stop words......')
stop={}
with open("C:\\Users\\t-yunche\\file\\dataset\\stop_words.txt",'r',encoding='utf8') as f:
    lines=f.readlines()
    for s in lines:
        stop.setdefault(s[:-1],0)

'''
word preprocess
'''
print("title+body processing......")

dir_name= "C:\\Users\\t-yunche\\file\\dataset\\topic_clean"
with open(os.path.join(dir_name,'raw' ,str(sys.argv[1]) + '.tsv'), 'r', encoding='utf8') as f_r:

    word_dict={}
    rule=re.compile(u"[^a-zA-Z]")
    f=open(os.path.join(dir_name,'X_Y',str(sys.argv[1])+".tsv"),'w+',encoding='utf8')
    time_start = time.time()
    i=0
    while True:
        i+=1
        if(i%1000==0):
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start=time_end
            print("processing paper:",i)

        data_i=f_r.readline()
        if not data_i:
            break
        data_i=data_i[:-1].split('\t')
        for idx in range(2):
            arr=data_i[idx].lower().split(' ')
            arr_=""
            for a in arr:
                a=rule.sub("",a)
                if(a=='' or a in stop.keys()):
                    continue
                a=wnl.lemmatize(a)#lemmatization
                if(arr_==""):
                    arr_=a
                else:
                    arr_+=" "+a
            data_i[idx]=arr_
        f.write('\t'.join(data_i)+'\n')

    f.close()






