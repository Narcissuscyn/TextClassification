# import pandas as pd
# import re
# import sys
# from nltk.stem import WordNetLemmatizer
# wnl = WordNetLemmatizer()
#
#
# import time
#
# '''
# get label file
# '''
# print("loading the label data....")
# label_dict={}
# with open('./label_th10.txt','r',encoding='utf8') as f:#label index start from 0
#     labels=f.readlines()
#     for idx,label in enumerate(labels):
#         label_dict[label[:-1]]=str(idx)
# f.close()
#
#
# '''
# get stop words list
# '''
# # stop=stopwords.words('english')
# stop=[]
# with open("C:\\Users\\t-yunche\\file\\dataset\\stop_words.txt",'r') as f:
#     stop=f.readlines()
# stop=[s[:-1] for s in stop]
# f.close()
#
#
# '''
# get source data file
# '''
# file_name="C:\\Users\\t-yunche\\file\\dataset\\topic\\source\\"
# print("loading the source data...")
# data=pd.read_csv(file_name+str(sys.argv[1])+'.tsv',delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
#
#
# '''
# text preprocess
# '''
# word_dict={}
# rule=re.compile(u"[^a-zA-Z ]")
# print(data.shape)
# print("data process...")
# f=open("C:\\Users\\t-yunche\\file\\dataset\\topic\\X_Y\\"+str(sys.argv[1])+".tsv",'w+')
# time_start = time.time()
# for i,d in enumerate(data.iterrows()):
#
#     if(i%1000==0):
#         time_end = time.time()
#         print('time cost', time_end - time_start, 's')
#         time_start=time_end
#         print("iterrows:",i)
#
#     data_i=d[1].array
#
#     # topic=>label list
#     topic = data_i[-1]
#     topic = topic.split(', ')
#     topic_i = ""
#     for a in topic:
#         a = rule.sub("", a)
#         if (a == ''):
#             continue
#         if(' ' not in a):
#             a = wnl.lemmatize(a)  # lemmatization
#         if (a in label_dict.keys()):
#             a=label_dict[a]
#             if (topic_i == ""):
#                 topic_i =a
#             else:
#                 topic_i += ',' + a
#     if(topic_i==""):
#         continue
#     # title+body=>text_list
#     arr=data_i[0]+' '+data_i[1]
#     arr=arr.split(' ')
#     arr_=""
#     for a in arr:
#         a=rule.sub("",a)
#         if(a=='' or a in stop):
#             continue
#         # if(not en_dict.check(a)):#spelling check
#         #     b=en_dict.suggest(a)
#         #     if b==[]:
#         #         continue
#         #     a=b[0]
#         # print(a,'-->')
#         a=wnl.lemmatize(a)#lemmatization
#         if(arr_==""):
#             arr_=a
#         else:
#             arr_+=" "+a
#
#     f.write(arr_+'\t'+topic_i+'\n')
#
# f.close()
# del data
#
#
#
#
#
#


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






