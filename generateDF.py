#!/bin/python

import sys
import os
import re
from utils import getWordList, getWordCount

if len(sys.argv) > 1:
	dir = sys.argv[1]
else:
	sys.exit("Usage: python %s [directory]"%(sys.argv[0]))

WordList = []	
for filename in os.listdir(dir):
	WordList.extend(list(set(getWordList(os.path.join(dir,filename)))))
	
WordCount = getWordCount(WordList)

with open("df.dict", "w") as F:
	F.writelines([(word+" "+str(WordCount[word])+"\n").encode('utf8') for word in WordCount])
	
