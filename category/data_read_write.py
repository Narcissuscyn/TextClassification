
import sys
in_path=sys.argv[1]
urls=[]
with open(in_path,'r',encoding="utf8") as f:
    while True:
        line=f.readline()
        line=line.split('\t')
        urls.append(line)


pars={}
pars['SampleOutput']=urls
