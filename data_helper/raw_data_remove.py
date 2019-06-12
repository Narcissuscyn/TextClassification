print("loading labels.....")

labels=[]

with open('C:\\Users\\t-yunche\\file\\code\\data_helper\\ful_lbl_lst_del.txt','r',encoding='utf8') as f_r:
    labels=f_r.readlines()
    labels=[labels[i][:-1] for i in range(len(labels))]

with open("FJB_Merge.tsv", 'r', encoding='utf8') as f_r:
    with open('FJB_Merge_remove.tsv','w+',encoding='utf8') as f_w:
        while (True):
            a = f_r.readline()
            if not a:
                break
            a = a.split('\t')

            b = a[2][:-1].split(', ')
            a[2]=[]
            for l in b:
                if l in labels:
                    if a[2]==[] :
                        a[2]=l
                    else:
                        a[2]+=', '+l
            # if(len(b)>10):
            #     print(b)
            #     print(a[2])
            #     print("move before:",len(b),'->move after:',len(a[2].split(', ')))
            if(a[2]!=[]):
                f_w.write(('\t'.join(a))+'\n')
