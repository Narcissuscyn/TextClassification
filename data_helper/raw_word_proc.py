import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import os
import numpy as np
import sys
import time
import nltk
np.random.seed(2018)
nltk.download('wordnet')
stemmer = PorterStemmer()
char_thresh=2
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > char_thresh:
            result.append(lemmatize_stemming(token))
    return result


'''
word preprocess
'''
print("title+body processing......")

dir_name= "D:\\dataset\\FlipBoard_6k"
with open(os.path.join(dir_name,'raw' ,str(sys.argv[1]) + '.tsv'), 'r', encoding='utf8') as f_r:

    if not os.path.exists(os.path.join(dir_name,'X_Y')):
        os.mkdir(os.path.join(dir_name,'X_Y'))
    f=open(os.path.join(dir_name,'X_Y',str(sys.argv[1])+".tsv"),'w+',encoding='utf8')
    time_start = time.time()
    i=0
    while True:
        i+=1
        if(i%1000==0):
            time_end = time.time()
            print('time cost', time_end - time_start, 's')
            time_start=time_end
            print("processing paper:",i)

        data_i=f_r.readline()
        if not data_i:
            break
        data_i=data_i[:-1].split('\t')
        #title then body
        for idx in range(2):
            tx=preprocess(data_i[idx].lower())
            data_i[idx]=' '.join(tx)

        f.write('\t'.join(data_i)+'\n')

    f.close()
