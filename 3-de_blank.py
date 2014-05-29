#coding=utf-8
import os
import sys
import re
import time

f1=open("/home/alber/data_base/jd_content/app-mac/mac-result1.txt",'r+')
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result2.txt","a")
txt=f1.readlines()
f1.close()
list1=[]
for line in txt:
	line_clean=" ".join(line.split())
	lines=line_clean+" "+"\n"
	f2.write(lines)
f2.close()