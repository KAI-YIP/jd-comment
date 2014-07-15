# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys

dict = {'形':40,'条':70,'C':30,'D':85}
for i , key in enumerate(dict):
	plt.bar(i,dict[key])#i为0,1,2,3,指的是第i条条形
plt.xticks(np.arange(len(dict))+0.4,dict.keys())
plt.yticks(dict.values())
plt.show()