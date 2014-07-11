#coding utf-8
import os
import sys
import re

f1=open("/home/alber/KuaiPan/data_base/jd_content/app-mac/mac-result1.txt",'r')
txt=f1.readlines()
f1.close()
txtlist=[]
noun=["/n","/ns","/nt","/nz","/ng"]
verb=["/v","/vd","/vn","/vshi","/vyou","/vf","/vx","/vi","/vl","/vg"]
odjective=["/a","/ad","/an","/ag","/al"]
other=["/l","/eng","/m","/mq","/t","/tg","/f","/s"]
cixing=noun+verb+odjective+other
for line in txt:
	line_list2=re.split('[ ]', line)
	for seg in line_list2:
		for k in cixing:
			if k in seg:
				txtlist.append(seg)
			else:
				pass
	txtlist.append("\n")
wordlist=[]
for v in txtlist:
	if "/" in v:
		position=v.index("/")
		wordlist.append(v[:position])
	else:
		wordlist.append(v)
f2=open("/home/alber/KuaiPan/data_base/jd_content/app-mac/mac-N-V-Adj.txt",'a')
for segs in wordlist:
	f2.write(segs+" ")
f2.close()

