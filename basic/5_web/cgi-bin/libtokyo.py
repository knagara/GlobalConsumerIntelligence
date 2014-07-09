#!/usr/bin/python
# -*- coding:utf-8 -*-
import cgi
import urllib, urllib2, sys
import xml.etree.ElementTree as etree

print 'Content-type: text/html\n'
print """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>図書館in東京</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
          <div class="jumbotron">
        <h1>図書館 in 東京</h1>
        <p>東京にある図書館を検索することができます。</p>

      <section class="container">
        <div class="row">
        <div class="col-xs-10 col-sm-6 col-md-4">
        <form class="form-signin" role="form" method="post" action="libtokyo.py">
        <h2 class="form-signin-heading">市区町村名で検索</h2>
        <input name="message" type="text" class="form-control" placeholder="文京区" required autofocus>
        <input class="btn btn-lg btn-primary btn-block" type="submit" name="submit" value="検索">
      </form>
      </div>
        </div>
      </section>
      </div>
"""

message = ""
form = cgi.FieldStorage()
message = form.getvalue('message', '')
l = len(unicode(message,'utf-8')) if message else 0

if(message==""):
	#message="文京区"
	print """
 <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>

"""
else:

	#url = 'http://api.calil.jp/library?appkey=5f461f5176e75b1a500a8522adc8fd20&pref=東京都&city=%s'%message


	pref = u'東京都'
	urlprefix = 'http://api.calil.jp/library?'
	query = [
		('appkey', '5f461f5176e75b1a500a8522adc8fd20'),
	    ('pref', pref.encode('utf-8')),
	    ('city', message),
	]
	url = urlprefix + urllib.urlencode(query)

	#print url

	resp = urllib2.urlopen(url).read()
	output = []
	tree = etree.fromstring(resp)

	for item in tree.getiterator("Library"):
		#print item.findtext("short")
		output.append({
		        "name": item.findtext("short"),
		        "address": item.findtext("address"),
		        "tel": item.findtext("tel"),
		})

	#print output

	print """
	      <section class="container">
	        <div class="row">
	        <div class="col-xs-12 col-sm-12 col-md-12">
			<table class="table">
			  <thead>
			    <tr>
			      <th>名称</th>
			      <th>住所</th>
			      <th>TEL</th>
			    </tr>
			  </thead>
			  <tbody>
	"""

	for out in output:
		print '<tr><td>'+out['name'].encode('utf-8')+'</td><td>'+out['address'].encode('utf-8')+'</td><td>'+out['tel'].encode('utf-8')+'</td></tr>'

	print """
			  </tbody>
			</table>
	      </div>
	        </div>
	      </section>
	 <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	    <!-- Include all compiled plugins (below), or include individual files as needed -->
	    <script src="js/bootstrap.min.js"></script>
	  </body>
	</html>

	"""
