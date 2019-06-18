freq_thresh=5
freq={}
with open("./res/FJB_Merge.tsv", 'r', encoding='utf8') as f_r:
        while(True):
            a = f_r.readline()
            if not a:
                break
            a = a.split('\t')

            a=a[2][:-1].split(', ')
            for l in a:
                if l not in freq.keys():
                    freq[l]=0
                freq[l]+=1

# #
# print("move before: ",freq.__len__())
# keys=list(freq.keys())
# for key in keys:
#     if(freq[key]<freq_thresh):#labels whose frequency<freq_thresh are removed
#         freq.pop(key)
# print("move after: ",freq.__len__())
#


freq = sorted(freq.items(), key=lambda x: x[1],reverse=True)#sort the label according to its frequency
for idx, item in enumerate(freq):
    print(idx,item)
# with open("res/ful_lbl_lst.txt", 'w+', encoding='utf8') as f_w:
#     for idx,item in enumerate(freq):
#         print(item)
#         f_w.write((item[0]+'\n'))

