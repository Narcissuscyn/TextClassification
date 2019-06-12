
import random
with open('C:\\Users\\t-yunche\\file\\code\\data_helper\\res\\FJB_Merge_remove.tsv','r',encoding='utf8') as f_r:
    with open('./res/FJB_Merge_remove_shuffle.tsv','w+',encoding='utf8') as f_w:
        raw_datas=f_r.readlines()
        random.shuffle(raw_datas)

        for data in raw_datas:
            f_w.write(data)
