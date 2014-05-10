#coding: utf8
for i in range(1900,2201):
  if i%4 == 0:
    if i%400 == 0:
      print i ,
    elif i%100 != 0:
      print i ,
