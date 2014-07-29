#coding=utf-8  
import os
import sys
import nltk
import matplotlib as plt
from nltk.tokenize import *
from nltk.probability import *
import matplotlib.pyplot as plt



wordmap=open('/home/alber/data_base/chinese.txt','r')
wordmap1=wordmap.read().decode('utf-8')
data=nltk.tokenize.word_tokenize(wordmap1)
fdist1=FreqDist(data)
for k,v in fdist1.items():
	print k.encode('utf-8'),v
fdist1.plot(50)
