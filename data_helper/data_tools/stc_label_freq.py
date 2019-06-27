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

data_dir='C:\\Users\\t-yunche\\file\\dataset\\topic_clean\X_Y'

label_list=[]
i=1
while(i<7):
    file=os.path.join(data_dir,str(i)+'.tsv')
    print("loading file ", file)
    data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
    print(data.shape)
    label_list.extend(data[2])
    del data
    i+=1
print(label_list[:10])
print("statistc....")

f=open("./res/label_freq_clean_th5.txt",'w+',encoding='utf8')
data_freq={}
for i,label in enumerate(label_list):
    # if(i>1000):
    #     break
    label=label.split(',')
    for l in label:
        data_freq.setdefault(l,0)
        data_freq[l]+=1

print("writing data...")
# data_freq=np.array(data_freq)
# tick_l=np.argsort(-data_freq).tolist()
# data_freq=data_freq[tick_l]
# for i in range(len(data_freq)):
#     if(data_freq[i]>0):
#         f.write(str(i+1)+':'+str(data_freq[i])+'\n')
# f.close()

data_freq = sorted(data_freq.items(), key=lambda x: x[1],reverse=True)
data_values=[data[1] for data in data_freq]

max_len=1000
x=list(range(0,max_len))

print("drawing data...")
fig=plt.figure()
# plt.xticks(x)
plt.bar(x,data_values[:max_len],color="blue")

plt.xlabel("labbel-num")
plt.ylabel("label-freq")
plt.title("label statistic")
plt.savefig("./res/label_freq_clean_th5.jpg")
plt.show()
