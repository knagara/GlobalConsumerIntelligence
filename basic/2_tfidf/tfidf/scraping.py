#coding: utf8
import re

filename = '2010'
f = open('./text/'+filename+'.txt')
text = f.read()
f.close()

r = re.compile("context2.fillText\(\'.*?\'")
matchList = r.findall(text)
#print matchList

output = []
for w in matchList:
	s = w.split("\'")
	output.append(s[1])

f = open('./lyrics/'+filename+'.txt','w')
for x in output:
	f.write(str(x)+"\n")
f.close()