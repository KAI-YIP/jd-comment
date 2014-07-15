#coding=utf-8
import re
import math
import numpy as np

def vector_found(txt):
	word_list=[]
	for line in txt:
		line_clean=line.split()
		for word in line_clean:
			if word not in word_list:
				word_list.append(word)
			else:
				pass

	return word_list

def f_document_vector(document,word_list):
	vector=[]
	document_clean=document.split()
	for word in word_list:
		a=document_clean.count(word)
		vector.append(a)
	return vector

def svd_calculate(document_array):
	U,S,V=np.linalg.svd(document_array)
	return (U,S,V)

f=open("/home/alber/experiment/test.txt",'r')
txt=f.readlines()
f.close()
word_vector=vector_found(txt)
print (len(word_vector))
document=[]
Num_line=0
for line in txt:
	Num_line=Num_line+1
	document_vector=f_document_vector(line,word_vector)
	document.append(document_vector)
print (len(document))
U,S,V=svd_calculate(document)


f2=open("/home/alber/experiment/20140715/svd-v-result.txt",'a')
for line in U:
	for word in line:
		f2.write(str(word)+" ")
	f2.write('\n')
f2.close()
