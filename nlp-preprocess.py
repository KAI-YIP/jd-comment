#coding=utf-8
import os
import sys
import re
import time

def open_file(string):
	"""open the txt file to process"""
	f=open(string,'r')
	txt=f.readlines()
	return txt


def save_file(string,list_txt):
	"""save the result into a txt"""
	f2=open(string,'a')
	for line in list_txt:
		f2.write(line)


def cixing_choose(txt0):
	"""choose the noun(and the verb,objective and others) for the text after segment the word"""
	txtlist=[]
	noun=["/n","/ns","/nt","/nz","/ng"]
	verb=["/v","/vd","/vn","/vshi","/vyou","/vf","/vx","/vi","/vl","/vg"]
	objective=["/a","/ad","/an","/ag","/al"]
	other=["/l","/eng","/m","/mq","/t","/tg","/f","/s","/x"]
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
		if line!=" ":
			list1.append(line)
		else:
			pass
	return list1

def lineself_copy(txt2):
	"""copy the line for Gibbs sampling"""	
	list3=[]
	for line in txt2:
		a=" ".join(line.split())
		line_extend=a+" "+a+" "+a+" "+a+" "+a+"\n"
		list3.append(line_extend)
	return list3

def cixing_filter(txt3):
	"""filter the word we don't need according the cixing"""
	txtlist=[]
	cixing=["/x","/zg","/uj","/ul","/e","/d","/uz","/y"]
	for line in txt3:
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


trace_sample="/home/alber/experiment/20140711/sample_result1.txt"
trace_result="/home/alber/experiment/20140711/sample_result2.txt"
file_txt=open_file(trace_sample)
txt0=cixing_choose(file_txt)
print txt0[:4]
txt1=de_blank(txt0)
print txt1[:4]
save_file(trace_result,txt1)
