# -*- coding: utf-8 -*-


def abs(a,b):
	if a>b:
		return a-b
	else:
		return b-a

x1=input("a=")
x2=input("b=")
print (abs(int(x1),int(x2)))