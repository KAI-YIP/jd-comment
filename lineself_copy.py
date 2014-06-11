#coding utf-8
import os
import sys

f1=open("/home/alber/KuaiPan/data_base/jd_content/app-mac/lda/mac.txt","r")
txt=f1.readlines()
f1.close()
f2=open("/home/alber/KuaiPan/data_base/jd_content/app-mac/lda/mac-result.txt",'a')

for line in txt:
	a=" ".join(line.split())
	line_extend=a+" "+a+" "+a+" "+a+" "+a+"\n"
	f2.write(line_extend)
f2.close()