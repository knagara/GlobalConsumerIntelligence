#coding: utf8
import urllib2, sys
import xml.etree.ElementTree as etree

resp = urllib2.urlopen('http://headlines.yahoo.co.jp/rss/zdn_mkt-bus.xml').read()

#print resp

output = {}
tree = etree.fromstring(resp)

#print tree[0][0].text

for item in tree[0].findall('item'):
	print item.find('title').text

#output['lat'] = tree.find('coordinate').find('lat').text
#output['lng'] = tree.find('coordinate').find('lng').text

#print output