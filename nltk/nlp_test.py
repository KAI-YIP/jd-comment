#coding=utf-8  
import os
import sys
from nltk import *

f=open('/home/alber/data_base/jd_content/lenovo-b490a-NoStopwords.txt',"r")
text=f.read().decode('utf-8')
fdist1=FreqDist(text)
vocabulary1=fdist1.keys()
freword=vocabulary1[:50]
for word in freword:
	print word.encode('utf-8')
#fdist1.plot(50,cumulative=True)