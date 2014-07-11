#coding=utf-8  
import os
import sys
import nltk
import matplotlib as plt
from nltk.tokenize import *
from nltk.probability import *
import matplotlib
from nltk.corpus import PlaintextCorpusReader

wordmap=open('/home/alber/data_base/jd_content/lenovo-b490a-NoStopwords.txt','r')
wordmap1=wordmap.read().decode('utf-8')
data=nltk.tokenize.word_tokenize(wordmap1)
fdist1=FreqDist(data)
fdist1[:30]
