import json as js
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

info = []
with open('data/dblp-ref/dblp-ref-1.json', 'r') as fin:
    s = fin.readlines()
for ii in s:
    info.append(js.loads(ii[:-1]))

def bag_of_word(s):
    temp = re.sub('[^A-Za-z]', ' ', s)
    temp = temp.lower()
    words = word_tokenize(temp)
    ans = []
    for word in words:
        if word not in stopwords.words('english'):
            ans.append(word)
    return " ".join(ans)

for ii in info:
	if 'abstract' in ii:
		ii['abstract'] = bag_of_word(ii['abstract'])

with open('modified_data/dblp-ref-1-trans.json', 'w') as fout:
	for ii in range(len(info)):
		fout.write(js.dumps(info[ii]))
		fout.write('\n')