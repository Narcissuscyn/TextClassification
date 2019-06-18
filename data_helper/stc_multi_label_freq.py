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

data_dir='C:\\Users\\t-yunche\\file\\dataset\\topic\X_Y'

label_list=[]
# i=1
# while(i<7):
#     file=os.path.join(data_dir,str(i)+'.tsv')
#     print("loading file ", file)
#     data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
#     label_list.extend(data[1])
#     del data
#     i+=1

with open("D:\\dataset\\FlipBoard_6k\\X_Y\\all.tsv",'r',encoding='utf8') as f_r:
    while True:
        a=f_r.readline()
        if not a:
            break
        label_list.append(a.split('\t')[2])


f=open("./res/multi_label_frequency_6k.txt",'w+',encoding='utf8')
data_freq=[0]*200
max_len=0;
for i,label in enumerate(label_list):
    if(i%10000==0):
        print("data node:",i)
    len_=len(label.split(','))
    if(len_>max_len):
        max_len=len_
    # print(len_)
    # print(label)
    data_freq[len_]+=1

for i in range(max_len+1):
    if(data_freq[i]>0):
        f.write(str(i)+':'+str(data_freq[i])+'\n')
f.close()
fig=plt.figure()
max_len=min(35,max_len)
data_freq=np.array(data_freq[1:max_len+1])
x=list(range(1,max_len+1))
# plt.xticks(x)
plt.bar(x,data_freq,color="blue")
plt.xlabel("labbel-num")
plt.ylabel("label-freq")
plt.title("multi-label statistic")
plt.savefig("./res/multi_label_freq_6k.jpg")
plt.show()
