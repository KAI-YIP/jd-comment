#coding=utf-8
import os
import sys
import re
import time

f1=open("/home/alber/data_base/jd_content/cameraD90/CameraD90.txt",'r+')
f2=open("/home/alber/data_base/jd_content/cameraD90/CameraD90-result.txt","a")
txt=f1.readlines()
f1.close()
list1=[]
for line in txt:
	if len(line)>=2:
		line_clean=" ".join(line.split())
		lines=line_clean+" "+"\n"
		f2.write(lines)
	else:
		pass
f2.close()