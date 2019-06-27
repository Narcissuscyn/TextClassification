from nltk.corpus import wordnet as wn

import nltk
from nltk import*
import enchant
import time

from enchant.checker import SpellChecker

from nltk.stem import WordNetLemmatizer
LABEL_THRESH=3
st = LancasterStemmer()
import re
# nltk.download('wordnet')
LEN_THRESH=15
rule=re.compile(u"[^a-zA-Z-_]")
en_dict = enchant.DictWithPWL("en_US")
wnl = WordNetLemmatizer()
dict_wrong={}


label_proj={}

with open('my_words.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for line in lines:
        line=line[:-1].split(' ')
        label_proj[line[0]]=line[1]

with open('./wrong_list.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for l in lines:
        dict_wrong[l[:-1]]=1
dict_label={}
label_idx=0
time_start = time.time()

with open("D:\\dataset\\category_raw.tsv",'r',encoding='utf8') as f_r:
    with open('D:\\dataset\\category_label.tsv','w+',encoding='utf8') as f_w:
        i=0
        while True:
            i+=1
            if not i%10000:
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                time_start = time_end
                print("iterrows:", i)
            line=f_r.readline()
            if not line:
                break
            lines=line.split('\t')
            url=lines[0]
            url=url.lower().split('/')[3:]
            labels = []
            label_str = []
            dict_ls={}
            for i_idx,i_url in enumerate(url):
                if len(i_url)>LEN_THRESH or i_url in dict_wrong.keys():
                    continue
                i_url = rule.sub("", i_url)
                i_url = re.split('-| |_', i_url)
                for u in i_url:
                    if len(u)<3:
                        continue
                    if u in label_proj.keys():
                        u=label_proj[u]
                    if not en_dict.check(u) or u in dict_wrong.keys():
                        continue
                    u=wnl.lemmatize(u,'n')
                    if u in dict_ls.keys() or u in dict_wrong.keys():
                        continue
                    dict_ls[u]=1
                    synset=wn.synsets(u)
                    if synset==[]:
                        us=en_dict.suggest(u)
                        for u in us:
                            synset=wn.synsets(u)
                            if not synset==[]:
                                break
                    if synset == []:
                        continue

                    label_path = synset[0].hypernyms()
                    label_path.append(synset[0])
                    # print(u,'->',synset,'->',synset[0],'->',label_path)

                    max_num=1
                    num_hyp=len(label_path)
                    for idx in range(num_hyp):
                        label=label_path[num_hyp-idx-1].name().split('.')[0]
                        if max_num>LABEL_THRESH:
                            # print('label maximum...')
                            break
                        if label in dict_wrong.keys():
                            continue
                        max_num+=1
                        # print(max_num)
                        dict_label.setdefault(label,dict_label.keys().__len__())
                        labels.append(str(dict_label[label]))
                        label_str.append(label)
            # print(labels.__len__())
            if labels==[]:
                continue
            lines[-1]=lines[-1][:-1]
            lines.append(','.join(labels))
            lines.append(','.join(label_str))
            f_w.write('\t'.join(lines)+'\n')

with open('./label_dicts.txt','w+',encoding='utf8') as f_w:
    for key in dict_label.keys():
        f_w.write(key+'\n')

# s1=wn.synsets("life")
# s2=wn.synsets("life_style")
# a=wn.synset('basketball.n.01')
# hyper=lambda s: s.hypernyms()
# print(list(a.closure(hyper)))
#
# w1 = wn.synset('life.n.01')
# w2 = wn.synset('life_style.n.01')
# print(w1.wup_similarity(w2))