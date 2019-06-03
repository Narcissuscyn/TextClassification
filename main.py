import pandas as pd
data=pd.read_csv("C:\\Users\\t-yunche\\file\\dataset\\test.tsv",sep='\t')
#print(data.__len__())
freq={}
for i,d in enumerate(data.iterrows()):
    arr=d[1].array
    #print(arr)
    #print(arr.shape)
    #print(arr[2])
    #if(i==412):
    #print(d)

    for a in arr[-2].split(' '):
        if a not in freq.keys():
            freq[arr[-2]]=0
        freq[arr[-2]]+=1
    if(arr.shape[0]!=4):
        #print(d)
        continue

print(freq)
#print(d)
