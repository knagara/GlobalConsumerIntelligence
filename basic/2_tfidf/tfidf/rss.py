#coding: utf-8
import urllib2, sys
import xml.etree.ElementTree as etree
from BeautifulSoup import BeautifulSoup as bsoup

"""　RSSリスト
Business Media 誠
http://headlines.yahoo.co.jp/rss/zdn_mkt-bus.xml
J-CASTニュース
http://headlines.yahoo.co.jp/rss/jct-bus.xml
SankeiBiz
http://headlines.yahoo.co.jp/rss/fsi-bus.xml
誠 Biz.ID
http://headlines.yahoo.co.jp/rss/zdn_b-bus.xml
ITmedia ニュース
http://headlines.yahoo.co.jp/rss/zdn_n-c_sci.xml
"""

url = "http://headlines.yahoo.co.jp/rss/zdn_n-c_sci.xml"
resp = urllib2.urlopen(url).read()

output = {}
tree = etree.fromstring(resp)

links = []
for item in tree[0].findall('item'):
	s = item.find('link').text.split('*')
	links.append(s[1])

for url in links:
	html = urllib2.urlopen(url).read()
	soup = bsoup(html)
	h1 = soup.find('h1', attrs={"class":"yjXL"}).contents
	text = soup.find('p', attrs={"class":"ynDetailText"}).contents
	f = open('./rss/'+str(h1[0])+'.txt','w')
	for t in text:
		f.write(str(t))
	f.close()