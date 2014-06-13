#coding: utf-8
#import urllib2, sys
#import xml.etree.ElementTree as etree
from BeautifulSoup import BeautifulSoup as bsoup

f = open('links.txt','w')
links = []
#url = "http://gyokai-search.com/2nd-genre.htm"
url = "http://cooksonia.6.ql.bz/test/gyokai.html"
html = urllib2.urlopen(url).read()
soup = bsoup(html)
links = soup.findAll('a')
for link in links:
	str_ = dict(link.attrs)['href']
	f.write(str_+"\n")

f.close()

"""
for url in links:
	html = urllib2.urlopen(url).read()
	soup = bsoup(html)
	h1 = soup.find('h1', attrs={"class":"yjXL"}).contents
	text = soup.find('p', attrs={"class":"ynDetailText"}).contents
	f = open('./rss/'+str(h1[0])+'.txt','w')
	for t in text:
		f.write(str(t))
	f.close()
"""