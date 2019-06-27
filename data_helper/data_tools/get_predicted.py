import os
import numpy as np
file_dir="C:\\Users\\t-yunche\\file\\code\\Tree_Extreme_Classifiers\\Tree_Extreme_Classifiers\\Sandbox\\Results"
dataset='topic_clean'
score_file=os.path.join(file_dir,dataset,'score_mat_p.txt')


print("loading the label data....")
label_dict={}
with open('./res/labellist_clean_th5.txt','r',encoding='utf8') as f:#label index start from 0
    labels=f.readlines()
    for idx,label in enumerate(labels):
        label_dict[idx]=label[:-1]
f.close()

with open(score_file,'r',encoding='utf8') as f_r:
    n_r,n_c=(f_r.readline()).split(' ')
    n_c=int(n_c[:-1])
    n_r=int(n_r)

    mat_score=[]
    mat_ind=[]
    while True:
        scores=f_r.readline()
        if not scores:
            break
        scores=scores[:-1].split(' ')
        score_list=[]
        score_ind=[]
        for score in scores:
            ft_score=score.split(':')
            score_ind.append(int(ft_score[0]))
            score_list.append(float(ft_score[1]))
        mat_score.append(score_list)
        mat_ind.append(score_ind)


k=5#get top 5 scored labels
with open(os.path.join(file_dir,dataset,'top_'+str(k)+'res_p.txt'),'w+',encoding='utf8') as f_w:


    for idx,l in enumerate(mat_score):
        l = np.array(l)
        l_idxs = np.array(mat_ind[idx])
        top_k_inds=np.argsort(-l)[:k]
        top_k_lbl_idx=l_idxs[top_k_inds]
        top_k_lbl_nam=""
        for lbl_i in top_k_lbl_idx:
            if(top_k_lbl_nam==''):
                top_k_lbl_nam=label_dict[lbl_i]
            else:
                top_k_lbl_nam+=', '+label_dict[lbl_i]
        f_w.write(top_k_lbl_nam+'\n')