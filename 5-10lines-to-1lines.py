#coding utf-8
import os
import sys

f1=open("/home/alber/data_base/jd_content/app-mac/mac-result3.txt",'r')
txt=f1.readlines()
f1.close()
txtlist=[]
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result4.txt",'a')
for line in txt:
	if len(line)<=2:
		pass
	else:
		txtlist.append(line)
count=0
wordlist=[]		
for line in txtlist:
	line_clean=" ".join(line.split())
	count=count+1
	if count!=9:
		line_clean=line_clean+" "
		wordlist.append(line_clean)
	if count==9:
		line_clean=line_clean+" "+"\n"
		wordlist.append(line_clean)
		count=0
for line in wordlist:
	f2.write(line)
f2.close()