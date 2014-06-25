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
	filelist = glob.glob('/Users/Keita/Documents/temp/Nature/*')
	histogram(filelist,0,X,y,ch)
	#都市 1
	filelist = glob.glob('/Users/Keita/Documents/temp/City/*')
	histogram(filelist,1,X,y,ch)

	parameters = {'kernel':['linear'], 'C':np.logspace(-4, 4, 10), 'gamma':np.logspace(-4, 4, 10)}
	clf = svm.SVC()
	#clf = svm.SVC(kernel='rbf',C=1000,gamma=0.001)
	clf = grid_search.GridSearchCV(clf, parameters, n_jobs = -1)
	clf.fit(X, y) #学習
	#print clf.predict([2,2,4]) #予測

	#0になるはず
	Z0 = []
	filelist = glob.glob('/Users/Keita/Documents/temp/Rural/*')
	for file_ in filelist:
		hist = getHist(file_)
		x = []
		for h in hist:
			x.append(h[0])
		Z0.append(clf.predict(x)[0])

	#1になるはず
	Z1 = []
	filelist = glob.glob('/Users/Keita/Documents/temp/Machi/*')
	for file_ in filelist:
		hist = getHist(file_)
		x = []
		for h in hist:
			x.append(h[0])
		Z1.append(clf.predict(x)[0])

	print Z0
	print Z1

	#TP,FN
	TP = 0
	FN = 0
	for i in Z1:
		if(i==1):
			TP+=1
		else:
			FN+=1
	print "TP = "+str(TP)+" FN = "+str(FN)

	#FP,TN
	FP = 0
	TN = 0
	for i in Z0:
		if(i==0):
			TN+=1
		else:
			FP+=1
	print "TN = "+str(TN)+" FP = "+str(FP)

	if((TP+FP)==0):
		Precision = 0
	else:
		Precision = float(TP)/float((TP+FP))

	if((TP+FN)==0):
		Recall = 0
	else:
		Recall = float(TP)/float((TP+FN))

	if((Precision+Recall)==0):
		F=0
	else:
		F = float(2*Precision*Recall)/float((Precision+Recall))

	print "F = "+str(F)




