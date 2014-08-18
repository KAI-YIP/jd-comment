#coding utf-8
import os
import sys
import re


f1=open("/home/alber/data_base/bigdata/movielens_train.txt",'r+')
matrix=f1.readlines()
f1.close()
i=1
commodity=["1,"]
for line in matrix:
	linelist=re.split('[,]', line)
	if linelist[0]==str(i) and len(linelist)>=2:
		good=linelist[1]+" "
		commodity.append(good)
	elif linelist[0]!=str(i) and len(linelist)>=2:
		i=i+1
		good="\n"+str(i)+","+linelist[1]+" "
		commodity.append(good)
	else:
		pass
print commodity
f2=open("/home/alber/data_base/bigdata/movielens_train_result.txt","a")
for v in commodity:
	f2.write(v)
f2.close()
