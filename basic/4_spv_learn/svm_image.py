# -*- coding: utf-8 -*-
import cv2
import pylab as plt
import numpy as np
import glob
from sklearn import svm, grid_search

def getHist(file_):
	img = cv2.imread(file_,cv2.IMREAD_COLOR)
	hist_item = cv2.calcHist([img],[1],None,[10],[0,255])
	cv2.normalize(hist_item,hist_item,0,100,cv2.NORM_MINMAX)
	hist=np.int32(np.around(hist_item))
	return hist

def histogram(filelist,class_,X,y,ch):
	for file_ in filelist:
		#print file_
		hist = getHist(file_)
		x = []
		for h in hist:
			x.append(h[0])
		X.append(x)
		y.append(class_)


if __name__ == '__main__':

	ch = 1
	X = []
	y = []

	#自然 0
	filelist = glob.glob('/Users/Keita/Documents/temp/Rural/*')
	histogram(filelist,0,X,y,ch)
	#都市 1
	filelist = glob.glob('/Users/Keita/Documents/temp/Machi/*')
	histogram(filelist,1,X,y,ch)

	#parameters = {'kernel':['rbf'], 'C':np.logspace(-4, 4, 10), 'gamma':np.logspace(-4, 4, 10)}
	clf = svm.SVC()
	#clf = grid_search.GridSearchCV(clf, parameters, n_jobs = -1)
	clf.fit(X, y) #学習
	#print clf.predict([2,2,4]) #予測

	#0になるはず
	Z0 = []
	filelist = glob.glob('/Users/Keita/Documents/temp/Nature/*')
	for file_ in filelist:
		hist = getHist(file_)
		x = []
		for h in hist:
			x.append(h[0])
		Z0.append(clf.predict(x)[0])

	#1になるはず
	Z1 = []
	filelist = glob.glob('/Users/Keita/Documents/temp/City/*')
	for file_ in filelist:
		hist = getHist(file_)
		x = []
		for h in hist:
			x.append(h[0])
		Z1.append(clf.predict(x)[0])

	print Z0
	print Z1




