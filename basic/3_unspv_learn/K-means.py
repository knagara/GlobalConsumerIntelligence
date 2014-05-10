#coding:utf-8
import random
from itertools import izip
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class MyKMeans():
	def __init__(self,init,n_clusters):
		self.init = init
		self.n = n_clusters

	#中心点の計算			
	def getCentroid(self):
		#座標の足しあわせ
		for i,X_ in enumerate(self.X):
			for j,value in enumerate(X_):
				self.centroid[self.labels_[i]][j] += value
		#クラスタの要素数の計算
		for i in self.labels_:
			self.labelCount[i] += 1
		for i,label in enumerate(self.centroid):
			for j,value in enumerate(label):
				self.centroid[i][j] /= self.labelCount[i]

	def distance(self,cent,xx):
		self.dist = 0
		for c,x in izip(cent,xx):
			self.dist += (c-x)**2
		return self.dist

	#各要素の分類
	def classify(self):
		for i,x in enumerate(self.X):
			self.dists = []
			for c in self.centroid:
				self.dists.append(self.distance(c,x))
			self.labels_[i] = self.dists.index(min(self.dists))

	#K-means法の実行
	def fit(self,X):
		self.X = X
		self.dim = X[0]
		self.labels_ = [0] * len(self.X)
		self.labelCount = [0] * self.n
		self.centroid = []
		for i in range(0,self.n):
			self.centroid.append([0]*len(self.dim))
		#初期化 - ランダムに分類
		for i,value in enumerate(self.X):
			self.labels_[i] = random.randint(0,(self.n-1))
		#初期化 - 中心点の計算
		self.getCentroid()
		#収束するまで繰り返し
		ii=0
		while ii<10:
			print self.centroid
			self.classify()
			self.getCentroid()
			#for i,value in enumerate(self.X):
			#	self.labels_[i] = 
			ii += 1
		print self.labels_


a=np.random.random((100,2))+2
b=np.random.random((100,2))+5
c=np.random.random((100,2))+8
X=np.concatenate((a,b,c))

#print X

my_kmeans = MyKMeans('random',3)
my_kmeans.fit(X)
Y=my_kmeans.labels_

plt.scatter(*zip(*X), c= my_kmeans.labels_, vmin=0, vmax=2, s=12)

plt.show()

"""
k_means= KMeans(init='random', n_clusters=3) #init：初期化手法、n_clusters=クラスタ数を指定
k_means.fit(X)
Y=k_means.labels_  #得られた各要素のラベル

#plt.figsize(10,5)
plt.scatter(*zip(*X), c= k_means.labels_, vmin=0, vmax=2, s=12)

plt.show()
"""