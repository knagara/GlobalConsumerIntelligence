#coding:utf-8
import glob
import MeCab
import copy

#ファイルから文章を取得
filelist = glob.glob('./text/*.txt')
text = []
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

#tfidfの計算
D = len(filelist) #文章の数
tf_sum = [] #tf分母
for i in wordCountLocal:
	tf_sum.append(sum(i.values()))
tfidf = copy.deepcopy(wordCountLocal)
for i,t in enumerate(tfidf):
	for word,count in t.items():
		tf = float(count)/tf_sum[i] #tfの計算
		idf = float(D)/wordCountGlobal[word] #idfの計算
		t[word] = tf * idf #tfidfの計算
	tfidf[i] = t

#結果表示
for i,t in enumerate(tfidf):
	print filelist[i],
	print '->',
	#---最大値のみ---
	#print max([(v,k) for k,v in t.items()])[1]
	#---ソートして3つまで---
	for j,item in enumerate(sorted(t.items(), key=lambda x:x[1], reverse=True)):
		print item[0]+",",
		j+=1
		if(j>=3):
			break
	print ""