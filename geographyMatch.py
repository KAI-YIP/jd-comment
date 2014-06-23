#coding utf-8
import os
import sys
import string

f1=open("/home/alber/KuaiPan/data_base/geogra_dic.txt",'r')
dic_txt=f1.readlines()
f1.close()
f2=open("/home/alber/KuaiPan/data_base/blog.txt",'r')
blogs=f2.readlines()
f2.close()
dic=[]
blog_match=[]
for line in dic_txt:
	line_low=line.lower()
	line_clean=" ".join(line_low.split())
	dic.append(line_clean)
