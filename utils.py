
import re
import jieba

def getWordList(filename):
	WordList = []
	reContent = re.compile("<content>(?P<content>.*)</content>")
	try:
		for line in open(filename):
			data = reContent.findall(line.strip().decode("gbk"))
			for item in data:
				WordList.extend(jieba.cut_for_search(item))
	except:
		print filename
		return []
	return WordList

def getWordCount(WordList):
	WordSet = set(WordList)
	WordCount = dict([(word,0) for word in WordSet])
	for word in WordList:
		WordCount[word] += 1
	return WordCount
	
def loadWordCount(dictname):
	WordCount = {}
	with open(dictname) as F:
		for line in F.readlines():
			line = line.strip().decode("utf8")
			if len(line.split()) == 2:
				word, count = line.split()
				word, count = word, int(count)
				WordCount[word] = count
	return WordCount
	
	
