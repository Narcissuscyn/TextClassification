import gensim
import os
processed_docs=[]
# labels=[]
i=1
data_dir='D:\\dataset\\MSN_NEWS\\X_Y'
while i<7:
    print('loading data file ',i,'...')
    with open(os.path.join(data_dir,str(i)+'.tsv'),'r',encoding='utf8') as f_r:
        while True:
            data=f_r.readline()
            if not data:
                break
            data =data.split('\t')
            data=data[0]+' '+data[1]
            processed_docs.extend([data.split(' ')])
    i+=1

print('getting dictionary...')
dictionary = gensim.corpora.Dictionary(processed_docs)
del processed_docs
print(dictionary.__len__())
print('filtering vocab...')
dictionary.filter_extremes(no_below=5, no_above=0.9,keep_n=None)
print(dictionary.__len__())
print('writing to file...')
with open('./res/vocab_msn.txt','w+',encoding='utf8') as f_w:
    for k in dictionary.keys():
        f_w.write(dictionary[k]+'\n')

