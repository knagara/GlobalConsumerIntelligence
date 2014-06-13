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
		self.maxCount = self.len*2 - 1
		self.dim = len(X[0])
		self.Z = []
		self.maxvalue = sys.maxint
		#self.maxvalue = 999
		self.D = np.ones([self.len,self.len])*self.maxvalue
		self.count = self.len
		self.cluster = {}
		#クラスタ辞書の初期化
		for i in range(0,self.len):
			self.cluster[i] = [i]
		self.clusterSum = {}
		#クラスタ要素数辞書の初期化
		for i in range(0,self.len):
			self.clusterSum[i] = 1

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
	
	#クラスタ辞書内の検索
	def getClusterNumber(self,value):
		num = 0
		for key in self.cluster:
			if value in self.cluster[key]:
				num = key
		return num

	#マージ
	def merge(self):
		#要素番号
		min_ij = np.argmin(self.D)
		min_i = int(min_ij/self.len)
		min_j = min_ij%self.len
		#クラスタ辞書内の検索
		min_i_cluster = self.getClusterNumber(min_i)
		min_j_cluster = self.getClusterNumber(min_j)
		#同じクラスタだった場合は除外
		if(min_i_cluster == min_j_cluster):
			#要素塗りつぶす
			self.D[min_i][min_j] = self.maxvalue
		else:
			#クラスタの要素数
			numOfCluster = self.clusterSum[min_i_cluster]+self.clusterSum[min_j_cluster]
			#Zに追加
			z = []
			z = [min_i_cluster,min_j_cluster,self.D[min_i][min_j],numOfCluster]
			self.Z.append(z)
	        #クラスタ辞書に追加
			clusterValues = []
			for i in self.cluster[min_i_cluster]:
				clusterValues.append(i)
			for i in self.cluster[min_j_cluster]:
				clusterValues.append(i)
			self.cluster[self.count] = clusterValues
			#クラスタ要素数辞書に追加
			self.clusterSum[self.count] = numOfCluster
			self.count+=1
			#要素塗りつぶす
			self.D[min_i][min_j] = self.maxvalue

	#実行
	def fit(self):
		#Distance Matrixの計算
		self.distMatrix()
		while 1:
			#self.printMat()
			self.merge()
			if(self.count == self.maxCount):
				break


### main ###
X = [[1,1],[3,3],[7,7],[8,8],[15,15],[20,20],[22,22],[37,37],[55,55],[60,60]]

myDendrogram = Dendrogram(X)
myDendrogram.fit()

for i in myDendrogram.Z:
	for j in i:
		print str(j).rjust(10),
	print ""

X = [[1,1],[3,3],[7,7],[8,8],[15,15],[20,20],[22,22],[37,37],[55,55],[60,60]]
p= pdist(X, metric="euclidean") #ユークリッド距離を採用する
Z= linkage(p, method="single") #最小最短距離法をmethodで指定する

print Z

dendrogram(Z)

plt.show()
