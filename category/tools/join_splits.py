def join_splits(files,tar_file):
    with open(tar_file,'w+',encoding="utf8")as f_w:
        for file in files:
            with open(file,"r",encoding='utf8') as f_r:
                while True:
                    l=f_r.readline()
                    if not l:
                        break
                    f_w.write('\t'.join(l.split('\t')[:-1])+'\n')

if __name__=='__main__':
    join_splits(["D:\\dataset\\MSN_NEWS\\raw\\category_raw_2017-05-31_2018-05-31.tsv","D:\\dataset\\MSN_NEWS\\raw\\category_raw_2016-05-31_2017-05-30.tsv"],'D:\\dataset\\MSN_NEWS\\raw\\news_msn_raw_extra.tsv')