
import os
print("loading the label data....")
label_dict={}
label_file='./res/labellist_clean_6000.txt'
dir_name="D:\\dataset\\topic_clean_wordlist"
with open(label_file,'r',encoding='utf8') as f:#label index start from 0
    labels=f.readlines()
    for idx,label in enumerate(labels):
        label_dict[label[:-1]]=str(idx)
f.close()

print('loading dataset......')
i=1
data_cnt=0
with open('D:\\dataset\\topic_clean_wordlist\\X_Y\\all.tsv','w+',encoding='utf8') as f_w:
    while(i<7):
        file=os.path.join(dir_name,'X_Y',str(i)+'.tsv')
        print("loading file ", file)
        # data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
        with open(file,'r',encoding='utf8') as f_r:
            while True:
                data=f_r.readline()
                if not data:
                    break
                data=data.split('\t')

                labels=data[2][:-1].split(', ')
                l_idx = ''
                for label in labels:
                    if label in label_dict.keys():
                        if l_idx == '':
                            l_idx = label
                        else:
                            l_idx += ', ' + label
                if l_idx == '':# if the topic is not in the label list,skip this dara point
                    continue

                data[2]=l_idx
                f_w.write('\t'.join(data)+'\n')
                data_cnt+=1
        i+=1
    print("data count:",data_cnt)
