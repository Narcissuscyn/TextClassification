import json


label_index={}


label_proj={}
with open('../tools/my_words.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for line in lines:
        line=line[:-1].split(',')
        label_proj.setdefault(line[0],line[1])



with open('labellist_msn.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()

    for idx,line in enumerate(lines):
        line=line[:-1]
        label_index.setdefault(line, idx)
with open('labeltree_son.json','r',encoding='utf8') as f_r:
    dict_son=json.load(f_r)
    dict_father={}
    for key in dict_son.keys():
        key_pre = key
        if key in label_proj.keys():
            key=label_proj[key]
        if key in label_index.keys():
            for item in dict_son[key_pre]:
                if item in label_proj.keys():
                    item=label_proj[item]
                if item==key:
                    continue
                if item in label_index.keys():
                    dict_father.setdefault(item,[])
                    if key in dict_father[item]:
                        continue
                    dict_father[item].append(key)
with open('label_index_msn.json','w+',encoding='utf8')as f_w:
    json.dump(label_index, f_w)

with open('labeltree_father.json','w+',encoding='utf8')as f_w:
    json.dump(dict_father, f_w)
