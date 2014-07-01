
import math

def selectWordByTfidf(tfWordCount, dfWordCount):
	thres = 1
	WordSelected = {}
	TfSum = sum(tfWordCount.values())
	TfMax = max(tfWordCount.values())
	DfSum = sum(dfWordCount.values())

	StopWords = [line.strip().decode("gbk") for line in open("stopwords.txt").readlines()]
	StopWords.extend([line.strip().decode("gbk") for line in open("stopwords-weibo.txt").readlines()])
	StopWords = set(StopWords)

	for word in tfWordCount:
		if tfWordCount[word] > thres and dfWordCount.has_key(word) and word not in StopWords and len(word) > 1:
			tf = 0.5*tfWordCount[word]/TfMax
			idf = math.log(DfSum/dfWordCount[word])
			WordSelected[word] = tf*idf
	WordSelected = [(k, int(WordSelected[k]*1000)) for k in WordSelected]
	WordSelected.sort(lambda x,y: int(x[1]<y[1])-int(x[1]>y[1]))
	WordSelected = WordSelected[:40]
	for k,v in WordSelected:
		print k, v
	return WordSelected