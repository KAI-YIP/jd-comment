#coding utf-8
import os
import sys
import time

t1=time.time()
support=0.01
f1=open("/home/alber/data_base/jd_content/app-mac/mac-result2.txt",'r')
content=f1.readlines()
f1.close()
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result3.txt",'a')
Num_lines=sum([lines.count("\n") for lines in content])
Num_blank=sum([lines.count(" ") for lines in content])
print Num_lines
for line in content:
	line=line.strip('\n')
	result=[]
	linelen = len(line)
	a=0
	for k in range(linelen) :
		if line[k:k+1]==" ":
			a=k+1
			result.append(a)
	for i in range(len(result)):
		if len(result)>2:
			if i==0:
				j1=int(result[1])-1
				target=line[0:j1]
			elif i<=(len(result)-2) and i>=1:
				j1=int(result[i-1])
				j2=int(result[(i+1)])-1
				target=line[j1:j2]
			elif i==len(result)-1:
				pass
			else:
				pass
			Num_target=sum([lines.count(target) for lines in content])
			Support=float(Num_target)/Num_lines
			if Support>=support:
				f2.write(target+"\n")
		else:
			pass
f2.close()
t2=time.time()
print str(t2-t1)
		

			


