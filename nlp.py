
import math

def selectWordByTfidf(tfWordCount, dfWordCount):
	thres = 1
	WordSelected = {}
	TfSum = sum(tfWordCount.values())
	TfMax = max(tfWordCount.values())
	DfSum = sum(dfWordCount.values())
	for word in tfWordCount:
		if tfWordCount > thres:
			tf = 0.5 + 0.5*tfWordCount[word]/TfMax
			idf = math.log(DfSum/dfWordCount[word])
			WordSelected[word] = tf*idf
	WordSelected = list(WordSelected)
	WordSelected.sort(lambda x,y: int(x[1]<y[1])-int(x[1]>y[1]))
	WordSelected = dict(WordSelected[:50])
	return WordSelected