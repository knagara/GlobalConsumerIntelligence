#coding: utf-8
import urllib2, sys
import xml.etree.ElementTree as etree

resp = urllib2.urlopen('http://headlines.yahoo.co.jp/rss/zdn_mkt-bus.xml').read()

output = {}
tree = etree.fromstring(resp)

for item in tree[0].findall('item'):
	print item.find('title').text
