#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import sys

f=open('/home/alber/experiment/20140719/dell_result1.txt','r')
txt=f.readlines()
f.close()
word_dict={}
for line in txt:
	line_clean=line.split()
	for word in line_clean:
		if word not in word_dict:
			word_dict[word]=1
		else:
			wordF=word_dict[word]+1
			word_dict[word]=wordF

word_frequency=sorted(word_dict.items(), key=lambda d: d[1],reverse=True)
print (word_frequency)

x=[]
y=[]
for k,v in word_frequency:
	y.append(v)
x=range(len(y))
print (len(x))
plt.xlabel("中文坐标")
plt.plot(x,y)
plt.show()