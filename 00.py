#coding utf-8
import os
import sys

f1=open("/home/alber/test.txt",'r')
content=f1.readlines()
f1.close()
for line in content:
	result=list()
	linelen = len(line)
	a=0
	for i in range(linelen) :
		if line[i:i+1]==" ":
			a=i+1
			result.append(a)
	print len(result)
	j1=int(result[1])
	j2=int(result[3])-1
	word=line[j1:j2]
	print word


