# -*- coding: utf-8 -*-
import cv2
import pylab as plt
import numpy as np

img = cv2.imread("lenna.jpg")
ch = 1
hist_item = cv2.calcHist([img],[ch],None,[10],[0,255])
cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
hist=np.int32(np.around(hist_item))
print hist
