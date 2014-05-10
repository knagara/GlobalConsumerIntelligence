#coding: utf8

def avg(x):
  return 1.0 * sum(x) / len(x)

def uruu(x):
  if x%4 == 0:
    if x%400 == 0:
      return True
    elif x%100 != 0:
      return True
    else:
      return False

data = [
  {"name":"田中花子","gender":"女性","score":58,"year":1980},
  {"name":"鈴木一郎","gender":"男性","score":76,"year":2000},
  {"name":"山田太郎","gender":"男性","score":69,"year":1989},
  {"name":"佐藤恵子","gender":"女性","score":62,"year":1992},
  {"name":"石井あや","gender":"女性","score":71,"year":1978}
]

scoresUruu = []
scoresNotUruu = []

for datum in data:
  if uruu(datum["year"]) == True:
    scoresUruu.append(datum["score"])
  else:
    scoresNotUruu.append(datum["score"])

print "うるう年に生まれた観客の平均評価点", avg(scoresUruu)
print "うるう年以外に生まれた観客の平均評価点", avg(scoresNotUruu)


