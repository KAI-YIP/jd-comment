#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import sys

f=open('/home/alber/NLP/20140719/dell_result1.txt','r')
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
x_word=[]
y=[]
count=0
for k,v in word_frequency:
	x_word.append(k)
	y.append(v)
	if count==50:
		break
	else:
		count+=1
x=range(len(y))
print (len(x))
plt.xlabel("中文坐标",color='green')
plt.plot(x,y)
plt.xticks(x,x_word)
for label in plt.gca().xaxis.get_ticklabels(): 
     label.set_rotation(90)
     label.set_ha('center')
     label.set_color('red')
plt.show()