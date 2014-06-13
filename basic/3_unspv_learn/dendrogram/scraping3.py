# -*- coding: utf-8 -*-
import codecs
import re
import urllib2, sys
from BeautifulSoup import BeautifulSoup as bsoup

rooturl = 'http://gyokai-search.com/'

fr = open('links.txt')
links = fr.readlines()
fr.close()

for url_ in links:
	url = rooturl + url_
	html = urllib2.urlopen(url).read().decode('shift_jis')
	soup = bsoup(html)
	h2 = soup.find('h2').contents
	h2list = h2[0].decode('shift_jis').split(u'　')
	f = open('./gyokai/'+str(h2list[0])+'.txt','w')
	texts = soup.findAll('li', attrs={"class":"basic"})
	for i,text in enumerate(texts):
		if(i<9):
			#print text
			#t = text.string.split(u'：')
			#f.write(str(t[0].encode('utf-8'))+',')
			#f.write(str(t[1].encode('utf-8'))+'\n')
			f.write(str(text)+'\n')
	f.close()

