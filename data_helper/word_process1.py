import pandas as pd
import re
import sys
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()


import time

'''
get stop words list
'''
# stop=stopwords.words('english')
stop=[]
with open("C:\\Users\\t-yunche\\file\\dataset\\stop_words.txt",'r') as f:
    stop=f.readlines()
stop=[s[:-1] for s in stop]
f.close()

'''
get source data file
'''

file_name="C:\\Users\\t-yunche\\file\\dataset\\topic\\"

print("loading the source data...")

data=pd.read_csv(file_name+str(sys.argv[1])+'.tsv',delimiter='\t',error_bad_lines=False,encoding='utf8',header=None)

'''
get label file
'''
print("loading the label data....")

label_dict={}
with open('./label.txt','r',encoding='utf8') as f:
    labels=f.readlines()
    for idx,label in enumerate(labels):
        label_dict[label[:-1]]=str(idx)
f.close()
# f=open("./data.txt",'w+')
#'!|\"|#|&|\'|(|)|*|+|,|.|/|:|;|<|=|>|?|@|[|\\|]|^|_|`|{|\||}|~|]|+|'
# chars=['[','\\',']','^','_','`','{','|','}','~',']','+','!','\"','#','%','&','\'','(',')','*','+'',','-','.','/',':',';','<','=','>','?','@','0','1','2','3','4','5','6','7','8','9']#'$'


'''
get text feature
'''
word_dict={}
rule=re.compile(u"[^a-zA-Z ]")
text_list=[]
label_list=[]
print(data.shape)
print("data process...")
f=open("C:\\Users\\t-yunche\\file\\dataset\\topic_X_Y\\"+str(sys.argv[1])+".tsv",'w+')
time_start = time.time()
for i,d in enumerate(data.iterrows()):
    if(i%1000==0):

        time_end = time.time()
        print('time cost', time_end - time_start, 's')
        time_start=time_end
        print("iterrows:",i)
    # feature_instance = []
    data_i=d[1].array

    # topic=>label list
    topic = data_i[-1]
    # if (topic is np.nan):
    #     # print(d)
    #     continue
    topic = topic.split(', ')#?
    topic_i = ""
    for a in topic:
        a = rule.sub("", a)
        if (a == ''):
            continue
        if(' ' not in a):
            a = wnl.lemmatize(a)  # lemmatization
        if (a in label_dict.keys()):
            a=label_dict[a]
            if (topic_i == ''):
                topic_i =a
            else:
                topic_i += ',' + a
    if(topic_i==''):
        continue
    # label_list.append(topic_i)

    # title+body=>text_list
    arr=data_i[0]+' '+data_i[1]
    arr=arr.split(' ')
    arr_=""
    for a in arr:
        a=rule.sub("",a)
        if(a=='' or a in stop):
            continue
        # if(not en_dict.check(a)):#spelling check
        #     b=en_dict.suggest(a)
        #     if b==[]:
        #         continue
        #     a=b[0]
        # print(a,'-->')
        a=wnl.lemmatize(a)#lemmatization
        if(arr_==""):
            arr_=a
        else:
            arr_+=" "+a


    # text_list.append(arr_)
    f.write(arr_+'\t'+topic_i+'\n')

f.close()
del data



print(text_list.__len__())
print(label_list.__len__())






