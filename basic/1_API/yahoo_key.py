#coding: utf8
import urllib2, sys
import xml.etree.ElementTree as etree

try: query = sys.argv[1]
except: query = '私の名前は永良慶太です。今年で23歳になります。好きな食べ物はガストのチーズINハンバーグです。'
resp = urllib2.urlopen('http://jlp.yahooapis.jp/KeyphraseService/V1/extract?appid=dj0zaiZpPTRZNXRHOTZQZWhwdCZzPWNvbnN1bWVyc2VjcmV0Jng9NTU-&sentence=%s'%query).read()

print resp

output = {}
tree = etree.fromstring(resp)

#output['lat'] = tree.find('coordinate').find('lat').text
#output['lng'] = tree.find('coordinate').find('lng').text

#print output