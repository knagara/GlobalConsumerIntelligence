#coding: utf8

def avg(x):
  return 1.0 * sum(x) / len(x)

data = [
  {"name":"田中花子","gender":"女性","score":58},
  {"name":"鈴木一郎","gender":"男性","score":76},
  {"name":"山田太郎","gender":"男性","score":69},
  {"name":"佐藤恵子","gender":"女性","score":62},
  {"name":"石井あや","gender":"女性","score":71}
]

male = 0
female = 0

for datum in data:
  if datum["gender"] == "男性":
    male += 1
  if datum["gender"] == "女性":
    female += 1
print male,female

scores = []
for datum in data:
  scores.append(datum["score"])
print 1.0 * sum(scores) / len(scores)
print avg(scores)


