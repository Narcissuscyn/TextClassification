
import pandas as pd
import time
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

file_name="C:\\Users\\t-yunche\\file\\dataset\\topic_mini\\X_Y"
text_list=[]
label_list=[]
i=1
while(i<7):
    file=os.path.join(file_name,str(i)+'.tsv')
    print("loading file ", file)
    data=pd.read_csv(file,delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)
    text_list.extend(data[0])
    label_list.extend(data[1])
    i+=1



#BOW feature：word_dict
print("get bow feature....")
vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(text_list)
# print(vectorizer.get_feature_names())
# print(bow)
# print(bow.toarray())

print("write bow feature to file")
tar_dir="C:\\Users\\t-yunche\\file\\dataset\\topic_mini\\ft"
f=open(os.path.join(tar_dir,"topic_mini_x_y.txt"),'w+',encoding='utf8')
f.write(str(bow.shape[0])+" "+str(bow.shape[1])+"\n")
# bow_=bow.toarray()
print(bow.shape)
# idx=-1
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

    f.write(label_list[i] + ' ')

    for idx, ft in enumerate(ind_ft):
        if(idx!=ind.__len__()-1):
            f.write(str(ind[idx]) + ":" + str(ft)+' ')
        else:
            f.write(str(ind[idx]) + ":" + str(ft)+'\n')

f.close()


#TF-IDF feature:
# tfidf2 = TfidfVectorizer()
# re = tfidf2.fit_transform(text_list)
# transformer = TfidfTransformer()
# tfidf =transformer.fit_transform(bow)
# print("tf-idf:\n",tfidf)
#

