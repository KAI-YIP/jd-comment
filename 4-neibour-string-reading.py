#coding utf-8
import os
import sys
import time
import re

t1=time.time()
support=4
coffidence=0.5
f1=open("/home/alber/data_base/jd_content/app-mac/mac-result4.txt",'r')
content=f1.readlines()
content_str=' '.join(content)
f1.close()
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result5.txt",'w')
Num_lines=sum([lines.count("\n") for lines in content])
iteration=0
wordlist=[]
print Num_lines
for line in content:
	iteration=iteration+1
	print "iteration %d"%(iteration)
	line=line.strip('\n')
	result=[]
	linelen = len(line)
	a=0
	for k in range(linelen):
		if line[k:k+1]==" ":
			a=k+1
			result.append(a)
	for i in range(len(result)):
		if len(result)>2:
			if i==0:
				j1=int(result[1])-1
				target=line[0:j1]
				if target not in wordlist:
					wordlist.append(target)
			elif i<=(len(result)-2) and i>=1:
				j1=int(result[i-1])
				j2=int(result[(i+1)])-1
				target=line[j1:j2]
				if target not in wordlist:
					wordlist.append(target)
			else:
				pass
		else:
			pass
iteration=0
for word in wordlist:
	f_word=re.split(r'\s+', word)
	word_before=f_word[0]
	word_after=f_word[1]
	if word_before!="tttttttt" and word_after!="tttttttt":
		Num_before=content_str.count(word_before)
		Num_after=content_str.count(word_after) 
		max_coff=max(Num_before,Num_after)
		Num_word=content_str.count(word)
		Support=float(Num_word)
		if Support>=support:
			Coffidence=float(Num_word)/max_coff
			if Coffidence>=coffidence:
				iteration=iteration+1
				print "counted %d"%(iteration)	
				f2.write(word+"\n")
			else:
				pass
		else:
			pass
	else:
		pass		
f2.close()
t2=time.time()
print str(t2-t1)