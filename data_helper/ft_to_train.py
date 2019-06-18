
import pandas as pd
import time
import os
dir_name= "D:\\dataset\\FlipBoard_6k\\ft"
print("loading data...")
data=pd.read_csv(os.path.join(dir_name, 'topic_x_y.txt'), sep='\t', error_bad_lines=False, encoding='utf8', header=None, skiprows=1)#skiprows:skip 1 row from top
# f=open(os.path.join(file_pth,'topic_x_y.txt'),'r')
# num_data,num_ft=f.readline()[:-1].split(' ')
# f.close()

print(data.shape)

print("spliting test and train file...")

f1=open(os.path.join(dir_name, 'trn_X_Xf.txt'), 'w+', encoding='utf8')
f2=open(os.path.join(dir_name, 'trn_X_Y.txt'), 'w+', encoding='utf8')
num_trn=int(data.shape[0]*0.8)
num_tst=data.shape[0]-num_trn
num_label=6000
# num_ft=2653075
# num_ft=2524528
num_ft=198169
f1.write(str(num_trn)+' '+str(num_ft)+'\n')
f2.write(str(num_trn)+' '+str(num_label)+'\n')
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

    if(not isTest and i==num_trn):
        train_cnt=i
        print("train data count:",i)
        f1 = open(os.path.join(dir_name, 'tst_X_Xf.txt'), 'w+', encoding='utf8')
        f2 = open(os.path.join(dir_name, 'tst_X_Y.txt'), 'w+', encoding='utf8')
        f1.write(str(num_tst) + ' ' + str(num_ft)+ '\n')
        f2.write(str(num_tst)+ ' ' + str(num_label)+ '\n')
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