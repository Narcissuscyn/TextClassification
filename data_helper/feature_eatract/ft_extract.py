#
# import pandas as pd
# import time
# import os
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# import numpy as np
#
#
# print("loading the label data....")
# label_dict={}
# label_file='./res/labellist_clean_6000.txt'
# dir_name="C:\\Users\\t-yunche\\file\\dataset\\topic_clean"
# ft_file=os.path.join(dir_name,'ft',"topic_x_y_6000.txt")
#
# with open(label_file,'r',encoding='utf8') as f:#label index start from 0
#     labels=f.readlines()
#     for idx,label in enumerate(labels):
#         label_dict[label[:-1]]=str(idx)
# f.close()
#
# print('loading dataset......')
#
#
#
# text_list=[]
# label_list=[]
# i=1
# while(i<7):
#     file=os.path.join(dir_name,'X_Y',str(i)+'.tsv')
#     print("loading file ", file)
#     # data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
#     with open(file,'r',encoding='utf8') as f_r:
#         while True:
#             data=f_r.readline()
#             if not data:
#                 break
#             data=data.split('\t')
#
#             labels=data[2][:-1].split(', ')
#             l_idx = ''
#             for label in labels:
#                 if label in label_dict.keys():
#                     if l_idx == '':
#                         l_idx = str(label_dict[label])
#                     else:
#                         l_idx += ',' + str(label_dict[label])
#             if l_idx == '':# if the topic is not in the label list,skip this dara point
#                 continue
#             label_list.append(l_idx)
#             text_list.append(data[0]+" "+data[1])
#     i+=1
#
#
#
# #BOW feature：word_dict
# print("get bow feature....")
# vectorizer = CountVectorizer()
# bow = vectorizer.fit_transform(text_list)
# # print(vectorizer.get_feature_names())
# # print(bow)
# # print(bow.toarray())
# print("writting bow feature to file")
# f=open(ft_file,'w+',encoding='utf8')
# f.write(str(bow.shape[0])+" "+str(bow.shape[1])+"\n")
# print(bow.shape)
# time_start=time.time()
# for i,item in enumerate(bow):
#
#     # print(item)
#     if(i%10000==0):
#         print("processing data point ",i,"....")
#         time_end = time.time()
#         print('time cost every 10000 data point:', time_end - time_start, 's')
#         time_start=time_end
#         print("iterrows:",i)
#     ind=sorted(item.indices)
#     ind_ft=item.todense()[:,ind].tolist()[0]
#
#     f.write(label_list[i] + ' ')
#
#     for idx, ft in enumerate(ind_ft):
#         if(idx!=ind.__len__()-1):
#             f.write(str(ind[idx]) + ":" + str(ft)+' ')
#         else:
#             f.write(str(ind[idx]) + ":" + str(ft)+'\n')
#
# f.close()
#
#
# #TF-IDF feature:
# # tfidf2 = TfidfVectorizer()
# # re = tfidf2.fit_transform(text_list)
# # transformer = TfidfTransformer()
# # tfidf =transformer.fit_transform(bow)
# # print("tf-idf:\n",tfidf)
# #


import pandas as pd
import time
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np


print("loading the label data....")
label_dict={}
with open('./res/lbl_6k.txt','r',encoding='utf8') as f:#label index start from 0
    labels=f.readlines()
    for idx,label in enumerate(labels):
        label_dict[label[:-1]]=str(idx)
f.close()

print('loading dataset......')

dir_name="D:\\dataset\\FlipBoard_6k"
text_list=[]
label_list=[]
i=1
while(i<2):
    # file=os.path.join(dir_name,'X_Y',str(i)+'.tsv')
    file=os.path.join(dir_name,'X_Y','all.tsv')

    print("loading file ", file)
    # data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
    with open(file,'r',encoding='utf8') as f_r:
        while True:
            data=f_r.readline()
            if not data:
                break
            data=data.split('\t')
            text_list.append(data[0]+" "+data[1])
            label_list.append(data[2][:-1])
    i+=1



#BOW feature：word_dict
print("get bow feature....")
vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(text_list)
# print(vectorizer.get_feature_names())
# print(bow)
# print(bow.toarray())
print("writting bow feature to file")
f=open(os.path.join(dir_name,'ft',"topic_x_y.txt"),'w+',encoding='utf8')
f.write(str(bow.shape[0])+" "+str(bow.shape[1])+"\n")
# bow_=bow.toarray()
print(bow.shape)
# idx=-1


# #TF-IDF feature
# print('getting tf-idf feature......')
# tfidf2 = TfidfVectorizer()
# tf_idf = tfidf2.fit_transform(text_list)
# print(tf_idf.get_feature_names())
#
# print("tf-idf shape:",tf_idf.shape)
# f=open(os.path.join(dir_name,'ft',"topic_x_y_tfidf.txt"),'w+',encoding='utf8')
# f.write(str(tf_idf.shape[0])+" "+str(tf_idf.shape[1])+"\n")

time_start=time.time()
for i,item in enumerate(bow):

    # print(item)
    if(i%10000==0):
        print("processing data point ",i,"....")
        time_end = time.time()
        print('time cost every 10000 data point:', time_end - time_start, 's')
        time_start=time_end
        print("iterrows:",i)
    ind=sorted(item.indices)
    ind_ft=item.todense()[:,ind].tolist()[0]

    labels=label_list[i].split(', ')
    l_idx=''
    for label in labels:
        if l_idx=='':
            l_idx=str(label_dict[label])
        else:
            l_idx+=','+str(label_dict[label])
    f.write(l_idx + ' ')

    for idx, ft in enumerate(ind_ft):
        if(idx!=ind.__len__()-1):
            f.write(str(ind[idx]) + ":" + str(ft)+' ')
        else:
            f.write(str(ind[idx]) + ":" + str(ft)+'\n')

f.close()


