#coding:utf-8
import os
import sys
import string
import time

t1=time.time()
f1=open("/home/alber/data_base/jd_content/app-mac/mac-result.txt",'r')
txt1=f1.readlines()
result=""
for line in txt1:
	if line.startswith(' '):
		if line.startswith('  '):
			if line.startswith('   '):
				if line.startswith('    '):
					result+=line[4:]
				else:
					result+=line[3:]
			else:
				result+=line[2:]
		else:
			result+=line[1:]

	else:
		pass
f2=open('/home/alber/data_base/jd_content/app-mac/mac-result1.txt','a')
f2.write(result)
f1.close()
f2.close()
t2=time.time()
print t2-t1
