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
i=1
while(i<7):
    file=os.path.join(data_dir,str(i)+'.tsv')
    print("loading file ", file)
    data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
    label_list.extend(data[1])
    del data
    i+=1

print("statistc....")

f=open("label-freq.txt",'w+',encoding='utf8')
data_freq=[0]*17000
for i,label in enumerate(label_list):
    # if(i>1000):
    #     break
    label=label.split(',')
    for l in label:
        data_freq[int(l)]+=1

print("writing data...")
data_freq=np.array(data_freq)
# tick_l=np.argsort(-data_freq).tolist()
# data_freq=data_freq[tick_l]
for i in range(len(data_freq)):
    if(data_freq[i]>0):
        f.write(str(i+1)+':'+str(data_freq[i])+'\n')
f.close()
max_len=1000
x=list(range(0,max_len))

print("drawing data...")
fig=plt.figure()
# plt.xticks(x)
plt.bar(x,data_freq[:max_len],color="blue")

plt.xlabel("labbel-num")
plt.ylabel("label freq")
plt.title("label statistic")
plt.savefig("./label_freq.jpg")
plt.show()
