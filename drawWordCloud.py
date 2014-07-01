#!/bin/python

import sys
import os
import re
from utils import getWordList, getWordCount, loadWordCount
from nlp import selectWordByTfidf
from draw import drawGraph

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	sys.exit("Usage: python %s [directory]"%(sys.argv[0]))

WordList = getWordList(filename)
tfWordCount = getWordCount(WordList)
for word in tfWordCount:
	print word, tfWordCount

dfWordCount = loadWordCount("df.dict")
WordSelected = selectWordByTfidf(tfWordCount, dfWordCount)
drawGraph(WordSelected, "picture.jpg")