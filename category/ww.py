import sys
import re
from shutil import copyfile

print("Number of arguments: ", len(sys.argv))
print("Argument List: ", str(sys.argv))

pars = {}
for arg in sys.argv:
    pair = (re.split('=|:', arg))
    if len(pair) > 1:
        pars[pair[0].lstrip('/')] = pair[1]

print(pars)
pars["SampleInput"]="D:\\code\\Aether\\Sample Data.tsv"
pars["SampleOutput"]="./res.tsv"
copyfile(pars["SampleInput"], pars["SampleOutput"])
print(pars["SampleParam"])