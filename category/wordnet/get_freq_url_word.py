import time


with open("D:\\dataset\\category_raw.tsv",'r',encoding='utf8') as f_r:
    with open('D:\\dataset\\category_label.tsv','w+',encoding='utf8') as f_w:
        i=0
        while True:
            i+=1
            if not i%10000:
                time_end = time.time()
                print('time cost', time_end - time_start, 's')
                time_start = time_end
                print("iterrows:", i)
            line=f_r.readline()