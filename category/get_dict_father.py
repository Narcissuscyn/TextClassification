import json
with open('./dict_son.json','r',encoding='utf8') as f_r:
    dict_son=json.load(f_r)
    dict_father={}
    for key in dict_son.keys():
        for item in dict_son[key]:
            dict_father.setdefault(item,[])
            dict_father[item].append(key)
        pass

with open('./dict_father.json','w+',encoding='utf8')as f_w:
    json.dump(dict_father, f_w)
