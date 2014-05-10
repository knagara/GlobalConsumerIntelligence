#coding:utf-8
import MeCab

sentence = "program item list item list item"

tagger = MeCab.Tagger()
result = tagger.parse(sentence)
print result

wordCount = {}
wordList = result.split()[:-1:2]

for word in wordList:
	wordCount.setdefault(word,0)
	wordCount[word]+=1

for word,count in wordCount.items():
	print '%-16s %i' % (word,count)