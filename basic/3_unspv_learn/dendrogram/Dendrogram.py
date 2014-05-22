#coding:utf8
import sys
import math
from itertools import izip
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

class Dendrogram():

	def __init__(self,X):
		self.X = X
		self.len = len(X)
		self.dim = len(X[0])
		self.Z = []
		self.maxvalue = sys.maxint
		self.maxvalue = 999
		self.D = np.ones([self.len,self.len])*self.maxvalue

	#距離の計算
	def distance(self,xx,yy):
		self.dist = 0
		for x,y in izip(xx,yy):
			self.dist += (x-y)**2
		return math.sqrt(self.dist)

	#Distance Matrixの計算
	def distMatrix(self):
		for i,x in enumerate(self.X):
			for j in range(0,i):
				self.D[i][j] = self.distance(self.X[i],self.X[j])

	#Distance Matrixのprint
	def printMat(self):
		for i in range(0,self.len):
			for j in range(0,self.len):
				print '%03d' % self.D[i][j] ,
			print ""

	#マージ
	def merge(self):
		#要素番号
		min_ij = np.argmin(self.D)
		min_i = int(min_ij/self.len)
		min_j = min_ij%self.len
		#クラスタの要素数
		numOfCluster = 2
		#Zに追加
		z = []
		z = [min_i,min_j,self.D[min_i][min_j],numOfCluster]
		self.Z.append(z)
		#要素塗りつぶす
		self.D[min_i][min_j] = self.maxvalue

	#実行
	def fit(self):
		self.distMatrix()
		self.printMat()
		self.merge()
		print self.Z


#a=np.random.random((10,5))+2
#b=np.random.random((10,5))+5
#c=np.random.random((10,5))+8
#X=np.concatenate((a,b,c))

X = [[1],[3],[7],[8],[15],[20],[22],[37],[55],[60]]
X = [[1,1],[3,3],[7,7],[8,8],[15,15],[20,20],[22,22],[37,37],[55,55],[60,60]]

print X

myDendrogram = Dendrogram(X)
myDendrogram.fit()

"""
x = np.argmin(X)
print x

a = np.array([[10,1,2], [3,4,5], [6,7,8]])
print np.argmin(a)
"""
"""
p= pdist(X, metric="euclidean") #ユークリッド距離を採用する
Z= linkage(p, method="single") #最小最短距離法をmethodで指定する

print Z

dendrogram(Z)

plt.show()
"""