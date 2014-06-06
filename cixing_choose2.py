#coding utf-8
import os
import sys
import re

f1=open("/home/alber/data_base/jd_content/app-mac/mac-result1.txt",'r')
txt=f1.readlines()
f1.close()
txtlist=[]
cixing=["/n","/ns","/nt","/nz","/ng"]
for line in txt:
	line_list2=re.split('[ ]', line)
	for seg in line_list2:
		for k in cixing:
			if k in seg:
				txtlist.append(seg)
			else:
				pass
wordlist=[]
for v in txtlist:
	position=v.index("/")
	wordlist.append(v[:position])
print wordlist
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result6.txt",'a')
nounlist=[]
for segs in wordlist:
	if segs not in nounlist:
		nounlist.append(segs)
		count=wordlist.count(segs)
		nounlist.append(" "+str(count)+"\n")
for noun in nounlist:
	f2.write(noun)
f2.close()