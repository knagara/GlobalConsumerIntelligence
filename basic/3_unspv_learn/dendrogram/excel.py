# -*- coding: utf-8 -*-
import codecs
import glob
import csv

#ファイルから文章を取得
filelist = glob.glob('./gyokai__/*.txt')
#CSV書き込み
fw = open('./gyokai__excel/gyokai.csv', 'ab') #ファイルが無ければ作る、の'a'を指定します
csvWriter = csv.writer(fw)

for file_ in filelist:
	f = open(file_)
	row = []
	gyokai = str(file_)[11:-4]
	row.append(gyokai)
	lines = f.readlines()
	for line in lines:
		row.append(float(line))
	csvWriter.writerow(row)
