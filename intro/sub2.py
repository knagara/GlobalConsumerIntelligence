#coding: utf8
def uruu(x):
  if x%4 == 0:
    if x%400 == 0:
      return True
    elif x%100 != 0:
      return True
    else:
      return False
