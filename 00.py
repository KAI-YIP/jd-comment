#coding utf-8
import os
import sys
import re
import matplotlib.pyplot as plt

f1=open("/home/alber/data_base/jd_content/app-mac/cipin.txt",'r')
txt=f1.readlines()
f1.close()
K=[]
V=[]
for line in txt:
	line_clean=line.split("	")
	K.append(line_clean[0])
	V.append(line_clean[1])
plt.plot(K,V)
plt.show()