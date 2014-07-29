#coding utf-8
import os
import sys
import time
import re

t1=time.time()
support=4
coffidence=0.5
f1=open("/home/alber/KuaiPan/data_base/laoxu/test.txt",'r')
content=f1.readlines()
content_str=' '.join(content)
f1.close()
f2=open("/home/alber/KuaiPan/data_base/laoxu/result4.txt",'w')
Num_lines=sum([lines.count("\n") for lines in content])
wordlist=[]
compound2=[]
print Num_lines

def items_set2(content,wordlist):
	iteration=0
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

def frequent_2items(content_str,wordlist,compound,support,coffidence,f2):				
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
					compound.append(word)
					print compound
				else:
					pass
			else:
				pass
		else:
			pass		

def frequent_3items(content_str,compound2,support):
	compoundword=" ".join(compound2)
	compoundword_list=compoundword.split(" ")
	for i in range(len(compoundword_list)-3):
		if i%2==0 and compoundword_list[i+1]==compoundword_list[i+2]:
			string=compoundword_list[i]+" "+compoundword_list[i+1]+" "+compoundword_list[i+3]
			Num_string=content_str.count(string)
			if Num_string>=support:
				f2.write(string)
			else:
				pass
		else:
			pass


items_set2(content,wordlist)
frequent_2items(content_str,wordlist,compound2,support,coffidence,f2)
f2.write("\n"+"\n")
frequent_3items(content_str,compound2,support)
f2.close()
t2=time.time()
print str(t2-t1)