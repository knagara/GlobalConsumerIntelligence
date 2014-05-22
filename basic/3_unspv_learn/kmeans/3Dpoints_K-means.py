#coding:utf-8
import random
from itertools import izip
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MyKMeans():
	def __init__(self,init,n_clusters):
		self.init = init
		self.n = n_clusters
		self.iteration = 10 #反復回数の初期値は10

	#反復回数の指定
	def setIteration(self,iteration):
		self.iteration = iteration

	#中心点の計算			
	def getCentroid(self):
		#中心座標初期化
		self.centroid = []
		for i in range(0,self.n):
			self.centroid.append([0]*len(self.dim))
		#座標の足しあわせ
		for i,X_ in enumerate(self.X):
			for j,value in enumerate(X_):
				self.centroid[self.labels_[i]][j] += value
		#クラスタの要素数の計算
		self.labelCount = [0] * self.n
		for i in self.labels_:
			self.labelCount[i] += 1
		#座標の平均値を求める
		for i,label in enumerate(self.centroid):
			for j,value in enumerate(label):
				self.centroid[i][j] /= self.labelCount[i]

	#距離の計算
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
		#初期化 - ランダムに分類
		for i,value in enumerate(self.X):
			self.labels_[i] = random.randint(0,(self.n-1))
		#初期化 - 中心点の計算
		self.getCentroid()
		#収束するまで繰り返し
		ii=0
		while ii<self.iteration:
			self.classify()
			self.getCentroid()
			ii += 1

#データ作成
a=np.random.random((10,3))+2
b=np.random.random((10,3))+5
c=np.random.random((10,3))+8
X=np.concatenate((a,b,c))

#k-means法の実行
my_kmeans = MyKMeans('random',3) #初期化方法、クラスタ数
my_kmeans.setIteration(30) #反復回数指定
my_kmeans.fit(X) #クラスタリング実行
Y=my_kmeans.labels_ #ラベル名取得

#plt.scatter(*zip(*X), c= my_kmeans.labels_, vmin=0, vmax=2, s=12)

#plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter3D(*zip(*X), c= my_kmeans.labels_, vmin=0, vmax=2, s=12)
plt.show()