#coding: utf8
import urllib2, sys
import xml.etree.ElementTree as etree

try: query = sys.argv[1]
except: query = '東京大学'
resp = urllib2.urlopen('http://www.geocoding.jp/api/?v=1.1&q=%s'%query).read()

#print resp

output = {}
tree = etree.fromstring(resp)

output['lat'] = tree.find('coordinate').find('lat').text
output['lng'] = tree.find('coordinate').find('lng').text

print output