# -*- coding: utf-8 -*-
import cv2
import pylab as plt
import numpy as np
import glob
from sklearn import svm

def getHist(file_):
	img = cv2.imread(file_,cv2.IMREAD_COLOR)
	hist_item = cv2.calcHist([img],[ch],None,[100],[0,255])
	cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
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
	filelist = glob.glob('/Users/Keita/Documents/temp/Nature/*')
	histogram(filelist,0,X,y,ch)
	#都市 1
	filelist = glob.glob('/Users/Keita/Documents/temp/City/*')
	histogram(filelist,1,X,y,ch)

	clf = svm.SVC(kernel='rbf') #Support Vector Classification(分類)、RBFカーネルを使用
	clf.fit(X, y) #学習
	#print clf.predict([2,2,4]) #予測



