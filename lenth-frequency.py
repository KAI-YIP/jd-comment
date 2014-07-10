#coding utf-8
import os
import sys
import matplotlib.pyplot as plt


f=open('/home/alber/experiment/20140704/sample-result3.txt','r')
lenth=[]
comment=f.readlines()
for line in comment:
	lenth_line=len(line)
	lenth.append(lenth_line)
y=lenth
plt.xlim(0,200)
plt.hist(y,1000)
plt.show()