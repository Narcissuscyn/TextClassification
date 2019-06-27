import os
import time
COUNT=210000
num=0
#8-splits
dir_idx=1

DATA_DIR="D:\\dataset\\MSN_NEWS\\raw"
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

f=open(os.path.join(DATA_DIR, str(dir_idx)+".tsv"),'w+',encoding='utf8')
time_start = time.time()
with open("res/FlipBoard_6k.tsv",'r',encoding='utf8') as f_r:
    i=-1
    while True:
        i+=1
        data_i=f_r.readline()
        if not data_i:
            break
        if(i%10000==0):
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start=time_end
            print("iterrows:",i)
        if(num==COUNT):
            print(i)
            dir_idx+=1
            f.close()
            f=open(os.path.join(DATA_DIR, str(dir_idx)+".tsv"),'w+',encoding='utf8')
            num=0
        f.write(data_i)
        num+=1

f.close
