#coding:utf-8
import MeCab
import copy

#ファイルから文章を取得
text = []
filelist = ['./text/sample1.txt','./text/sample2.txt','./text/sample3.txt','./text/sample4.txt','./text/sample5.txt']
for i in filelist:
	f = open(i)
	text.append(f.read())
#print text

#形態素解析
result = []
tagger = MeCab.Tagger()
for i in text:
	result.append(tagger.parse(i))

#単語の出現数を登録
wordCountGlobal = {}
wordCountLocal = []
for i in result:
	wordCount = {}
	wordList = i.split()[:-1:2]
	for word in wordList:
		wordCount.setdefault(word,0)
		wordCount[word]+=1
	wordCountLocal.append(wordCount)
	for word in wordCount.keys():
		wordCountGlobal.setdefault(word,0)
		wordCountGlobal[word]+=1

#tf,idfの計算
"""
#tf分母
tf_sum = []
for i in wordCountLocal:
	tf_sum.append(sum(i.values()))
#tf分子
tf = copy.deepcopy(wordCountLocal)
for i,tfj in enumerate(tf):
	for word,count in tfj.items():
		tfj[word] = float(count)/tf_sum[i]
	tf[i] = tfj
#idf
D = len(filelist)
idf = copy.deepcopy(wordCountLocal)
for i,idfj in enumerate(idf):
	for word,count in idfj.items():
		idfj[word] = float(D)/wordCountGlobal[word]
	idf[i] = idfj
#tfidfの算出
"""
D = len(filelist)
tf_sum = []
for i in wordCountLocal:
	tf_sum.append(sum(i.values()))
#tf分子
tfidf = copy.deepcopy(wordCountLocal)
for i,t in enumerate(tfidf):
	for word,count in t.items():
		tf = float(count)/tf_sum[i]
		idf = float(D)/wordCountGlobal[word]
		t[word] = tf * idf
	tfidf[i] = t

for word,count in tfidf[4].items():
	print '%-16s %f' % (word,count)