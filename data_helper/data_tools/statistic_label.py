
import numpy as np
import os
def label_count(src_file, dst_dir, split_flag=',', label_col=2, is_thresh=False, th=5):
    '''

    :param src_file: tsv or txt file name ,which is coloumned by '\t'
    :param dst_dir: labels sorted by frequncy in the descending order are saved in the txt file directory
    :param split_flag:the split flag for babels in coloumn(label_col)
    :param label_col: the column of the label
    :param is_thresh:wheather to file the labels with low frequency
    :param th: #labels whose frequency less than th are removed
    :return:label_freq
    '''
    label_freq={}
    mul_lab_freq={}
    with open(src_file, 'r', encoding='utf8') as f_r:
            while(True):
                a = f_r.readline()
                if not a:
                    break
                a = a.split('\t')
                a=a[label_col][:-1].split(split_flag)
                len_ = len(a)
                mul_lab_freq.setdefault(len_, 0)
                mul_lab_freq[len_] += 1
                for l in a:
                    if l not in label_freq.keys():
                        label_freq[l]=0
                    label_freq[l]+=1

    # compute Avg. Points per label
    Avg_per_lb = np.sum(list(label_freq.values())) / len(label_freq.keys())
    print("Avg. Points per label", Avg_per_lb)

    # compute Avg. Labels per point
    arr_key = np.array(list(mul_lab_freq.keys()))
    arr_val = np.array(list(mul_lab_freq.values()))
    Avg_per_data = (arr_key * arr_val).sum() / arr_val.sum()
    print("Avg. Labels per point", Avg_per_data)

    if is_thresh:
        print("move before: ",label_freq.__len__())
        keys=list(label_freq.keys())
        for key in keys:
            if(label_freq[key]<th):
                label_freq.pop(key)
        print("move after: ",label_freq.__len__())

    #write label frequency
    label_freq = sorted(label_freq.items(), key=lambda x: x[1],reverse=True)#sort the label according to its frequency
    with open(os.path.join(dst_dir,'label_freq.txt'), 'w+', encoding='utf8') as f_w:
        for idx,item in enumerate(label_freq):
            f_w.write((item[0]+' '+str(item[1])+'\n'))
    #write multi-label frequency
    label_freq = sorted(mul_lab_freq.items(), key=lambda x: x[1],reverse=True)#sort the label according to its frequency
    with open(os.path.join(dst_dir,'multi_label_freq.txt'), 'w+', encoding='utf8') as f_w:
        for idx,item in enumerate(label_freq):
            f_w.write((item[0]+' '+str(item[1])+'\n'))


