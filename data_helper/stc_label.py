import numpy as  np
label_freq={}
mul_lab_freq={}

with open("./res/FlipBoard_3k.tsv", 'r', encoding='utf8') as f_r:
        while(True):
            a = f_r.readline()
            if not a:
                break
            a = a.split('\t')

            a=a[2][:-1].split(', ')
            len_=len(a)
            mul_lab_freq.setdefault(len_,0)
            mul_lab_freq[len_]+=1
            for l in a:
                label_freq.setdefault(l, 0)
                label_freq[l]+=1


#compute Avg. Points per label
Avg_per_lb=np.sum(list(label_freq.values()))/len(label_freq.keys())
print("Avg. Points per label",Avg_per_lb)
#compute Avg. Labels per point

arr_key=np.array(list(mul_lab_freq.keys()))
arr_val=np.array(list(mul_lab_freq.values()))
Avg_per_data=(arr_key*arr_val).sum()/arr_val.sum()
print("Avg. Labels per point",Avg_per_data)
