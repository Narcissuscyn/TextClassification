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

print('loading word list')
word_dict={}
with open("./res/vocab.txt",'r',encoding='utf8') as f_r:
    word_list=f_r.readlines()
    for i in word_list:
        word_dict.setdefault(i[:-1],0)


# print(word_list)

'''
word preprocess
'''
print("title+body processing......")

dir_name= "D:\\dataset\\FlipBoard_6k"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
with open(os.path.join(dir_name,'X_Y','all_shuffle.txt'), 'r', encoding='utf8') as f_r:

    if not  os.path.exists(os.path.join(dir_name,'X_Y')):
        os.mkdir(os.path.join(dir_name,'X_Y'))
    f=open(os.path.join(dir_name,'X_Y',"all.tsv"),'w+',encoding='utf8')

    time_start = time.time()
    i=0
    while True:
        i+=1
        if(i%10000==0):
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start=time_end
            print("processing paper:",i)

        data_i=f_r.readline()
        if not data_i:
            break
        data_i=data_i.split('\t')
        # # topic=>label list
        # topic = data_i[-1]
        # topic = topic.split(', ')
        # topic_i = ""
        # for a in topic:
        #     a = rule.sub("", a)
        #     if (a == ''):
        #         continue
        #     if(' ' not in a):
        #         a = wnl.lemmatize(a)  # lemmatization
        #     if (a in label_dict.keys()):
        #         a=label_dict[a]
        #         if (topic_i == ""):
        #             topic_i =a
        #         else:
        #             topic_i += ',' + a
        # if(topic_i==""):
        #     continue

        #title then body
        for idx in range(2):
            arr=data_i[idx].split(' ')
            arr_=""
            for a in arr:
                if a not in word_dict.keys():
                    continue
                if(arr_==""):
                    arr_=a
                else:
                    arr_+=" "+a
            data_i[idx]=arr_
        if data_i[0]==''and data_i[1]=='':
            continue
        f.write('\t'.join(data_i))

    f.close()






