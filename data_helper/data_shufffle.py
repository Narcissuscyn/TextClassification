
import random
with open("res/FJB_Merge.tsv",'r',encoding='utf8') as f_r:
    with open('./res/FJB_Merge_shuffle.tsv','w+',encoding='utf8') as f_w:
        raw_datas=f_r.readlines()
        random.shuffle(raw_datas)

        for data in raw_datas:
            f_w.write(data)


# import os
# dir_name="D:\\dataset\\FlipBoard_6k"
# i=1
# raw_datas=[]
# while(i<7):
#     file=os.path.join(dir_name,'X_Y',str(i)+'.tsv')
#     # file=os.path.join(dir_name,'X_Y','all.tsv')
#     print("loading file ", file)
#     with open(file,'r',encoding='utf8') as f_r:
#         raw_datas.extend(f_r.readlines())
#     i+=1
# print(raw_datas.__len__())
# random.shuffle(raw_datas)
# print(raw_datas.__len__())
#
# with open(os.path.join(dir_name,'X_Y','all_shuffle.txt'), 'w+', encoding='utf8') as f_w:
#     for data in raw_datas:
#         f_w.write(data)