print("loading labels.....")

labels={}

with open('./res/lbl_6k.txt','r',encoding='utf8') as f_r:
    lines=f_r.readlines()
    for l in lines:
        labels.setdefault(l[:-1],0)
print("remove data with labels not in labels list...")
with open("./res/FJB_Merge_shuffle.tsv", 'r', encoding='utf8') as f_r:
    with open('./res/FlipBoard_6k.tsv','w+',encoding='utf8') as f_w:
        cnt=0
        while (True):
            a = f_r.readline()
            if not a:
                break
            a = a.split('\t')

            b = a[2][:-1].split(', ')
            a[2]=[]
            for l in b:
                if l in labels.keys():
                    if a[2]==[] :
                        a[2]=l
                    else:
                        a[2]+=', '+l
            # if(len(b)>10):
            #     print(b)
            #     print(a[2])
            #     print("move before:",len(b),'->move after:',len(a[2].split(', ')))
            if(a[2]!=[]):
                cnt+=1
                f_w.write(('\t'.join(a))+'\n')
        print("data count:",cnt)