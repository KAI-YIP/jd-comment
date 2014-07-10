# -*- coding: utf-8 -*-
import os
import sys

dou = u"，"
ju = u"。"
gan = u"！"
biaodian = ",.!" + dou + ju + gan

print(len(biaodian))
f1 = open("/home/alber/experiment/20140709/sample_result0.txt", 'r')
txt = f1.readlines()
f1.close()
f2 = open("/home/alber/experiment/20140709/sample_result2.txt", 'a')
for line in txt:
	print(line)
	line_clean = line.split()
	for word in line_clean:
		if word in biaodian:
		f2.write("\n")
	else:
		f2.write(word)
	
	f2.write("\n")