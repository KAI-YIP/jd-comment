#coding=utf-8
import os
import sys
import re
import time

def cixing_choose(txt0):
"""choose the noun(and the verb,objective and others) for the text after segment the word"""
	txtlist=[]
	noun=["/n","/ns","/nt","/nz","/ng"]
	verb=["/v","/vd","/vn","/vshi","/vyou","/vf","/vx","/vi","/vl","/vg"]
	objective=["/a","/ad","/an","/ag","/al"]
	other=["/l","/eng","/m","/mq","/t","/tg","/f","/s"]
	cixing=noun+verb+objective+other
	for line in txt0:
		line_list2=re.split('[ ]', line)
		for seg in line_list2:
			for k in cixing:
				if k in seg:
					txtlist.append(seg)
					break
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
	return wordlist


def de_blank(txt1):
"""delete the blank of the sample_test.txt"""
	list1=[]
	for line in txt1:
		if len(line)>=4:
			line_clean=" ".join(line.split())
			lines=line_clean+" "+"\n"
			list1.append(lines)
		else:
			pass
	return list1

def de_oneword_line(txt2):
"""delete the  line of txt whose lenth is leth than 2"""
	list2=[]
	for line in txt2:
		line_clean=line.split()
		if len(line_clean)>=2:
			line_new=" ".join(line_clean)+"\n"
			list2.append(line_new)
	return list2

def lineself_copy(txt3):
"""copy the line for Gibbs sampling"""	
	list3=[]
	for line in txt3:
		a=" ".join(line.split())
		line_extend=a+" "+a+" "+a+" "+a+" "+a+"\n"
		list3.append(line_extend)
	return list3

def cixing_filter(txt4):
"""filter the word we don't need according the cixing"""
	txtlist=[]
	cixing=["/x","/zg","/uj","/ul","/e","/d","/uz","/y"]
	for line in txt4:
		line_list2=re.split('[ ]', line)
		line_list=line_list2[:]
		for segs in line_list2:
			for K in cixing:
				if K in segs:
					line_list.remove(segs)
					break
				else:
					pass
		txtlist.extend(line_list)
	result_list=[]
	resultlist=txtlist[:]	
	for v in txtlist:
		if "/" in v:
			slope=v.index("/")
			letter=v[0:slope]+" "
			result_list.append(letter)
		else:
			result_list.append(v)
	return result_list


