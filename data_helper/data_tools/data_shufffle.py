import random
import os
# def shuffle_dataset(sou_file,tar_file):
#     with open(sou_file,'r',encoding='utf8') as f_r:
#         with open(tar_file,'w+',encoding='utf8') as f_w:
#             raw_datas=f_r.readlines()
#             random.shuffle(raw_datas)
#             for data in raw_datas:
#                 f_w.write(data)
def data_shuffle(sou_dir,sou_files,tar_dir,tar_file='all_shuffle.txt'):
    '''

    :param sou_dir:directory of file splits
    :param sou_files: file splits need to be joined bwfore shuffling
    :param tar_dir:target file directory
    :param tar_file:target file name
    :return:
    '''
    raw_datas=[]
    for file in sou_files:
        file=os.path.join(sou_dir,file)
        print("loading file ", file)
        with open(file,'r',encoding='utf8') as f_r:
            raw_datas.extend(f_r.readlines())
    print("shuffle before:",raw_datas.__len__())#2180690
    random.shuffle(raw_datas)
    print("shuffle after",raw_datas.__len__())
    if not os.path.exists(tar_dir):
        os.mkdir(tar_dir)
    with open(os.path.join(tar_dir,tar_file), 'w+', encoding='utf8') as f_w:
        for data in raw_datas:
            f_w.write(data)


if __name__=="__main__":
    tar_dir = "D:\\dataset\\MSN_NEWS\\annotated"
    data_shuffle(tar_dir,["category_msn.tsv"],tar_dir,"news_msn.tsv")