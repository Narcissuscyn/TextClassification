
import pandas as pd
import time
import os
file_pth="C:\\Users\\t-yunche\\file\\dataset\\topic\\ft"
print("loading data...")
data=pd.read_csv(os.path.join(file_pth,'topic_x_y.txt'),sep='\t',error_bad_lines=False,encoding='utf8',header=None,skiprows=1)#skiprows:skip 1 row from top
f=open(os.path.join(file_pth,'topic_x_y.txt'),'r')
num_data,num_ft=f.readline()[:-1].split(' ')
num_label='16965'
f.close()

print("spliting test and train file...")

f1=open(os.path.join(file_pth,'trn_X_Xf.txt'),'w+',encoding='utf8')
f2=open(os.path.join(file_pth,'trn_X_Y.txt'),'w+',encoding='utf8')

f1.write(num_data+' '+num_ft+'\n')
f2.write(num_data+' '+num_label+'\n')
isTest=False
time_start = time.time()
print("total data count:",data.shape[0])
train_cnt=0
for i,r in enumerate(data.iterrows()):
    if(i%50000==0):
        time_end = time.time()
        print('time cost', time_end - time_start, 's')
        time_start=time_end
        print("iterrows:",i)

    if(not isTest and i>0.8*data.shape[0]):
        train_cnt=i
        print("train data count:",i)
        f1 = open(os.path.join(file_pth, 'tst_X_Xf.txt'), 'w+', encoding='utf8')
        f2 = open(os.path.join(file_pth, 'tst_X_Y.txt'), 'w+', encoding='utf8')
        f1.write(num_data + ' ' + num_ft + '\n')
        f2.write(num_data + ' ' + num_label + '\n')
        isTest=True
    labels=r[1][0][:r[1][0].find(' ')].split(',')
    fts=r[1][0][r[1][0].find(' ')+1:]
    labels_r=""
    for id,l in enumerate(labels):
        if(id!=len(labels)-1):
            labels_r+=l+':1 '
        else:
            labels_r += l + ':1\n'
    f2.write(labels_r)
    f1.write(fts+'\n')
print("test data count:", i-train_cnt+1)

f1.close()
f2.close()