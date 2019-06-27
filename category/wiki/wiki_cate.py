# import gensim
# from nltk.stem import WordNetLemmatizer, SnowballStemmer
# from nltk.stem.porter import *
# import os
# import numpy as np
# import sys
# import time
# import nltk
# np.random.seed(2018)
# nltk.download('wordnet')

from nltk.corpus import wordnet as wn

import nltk
from nltk import*
import enchant

from enchant.checker import SpellChecker


s1=wn.synsets("life")
s2=wn.synsets("life_style")
a=wn.synset('basketball.n.01')
hyper=lambda s: s.hypernyms()
print(list(a.closure(hyper)))

w1 = wn.synset('life.n.01')
w2 = wn.synset('life_style.n.01')
print(w1.wup_similarity(w2))

# en_dict = enchant.DictWithPWL("en_US","mywords.txt")
# print(en_dict.check("tech"))
# print(en_dict.suggest("life"))
# print(en_dict.suggest("basktaball"))
#
# for s in wn.synsets("sports"):
#     # print("(",s.pos(),')',', '.join(l.name() for l in s.lemmas()))
#     print(s)




# string="tech."
# words=nltk.word_tokenize(string)
# print(nltk.pos_tag(words))
