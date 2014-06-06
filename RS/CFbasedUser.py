#coding utf-8
import os
import sys
import re

f1=open("/home/alber/data_base/bigdata/movielens_train_result.txt",'r')
f2=open("/home/alber/data_base/bigdata/movielens_train_result3.txt",'a')
txt=f1.readlines()
contxt=[]
f1.close()
userdic={}
for line in txt:
	line_clean=" ".join(line.split())
	position=line_clean.index(",")
	ID=line_clean[0:position]
	item=line_clean[position+1:]
	userdic.setdefault(ID,item)
	if len(item)>=5:
		contxt.append(item)
for key in userdic.keys():
	ID_num=key
	value=userdic[key]
  	user_item=value.split(' ')
  	Sim_user=[]
  	for lines in contxt:
  		lines_clean=lines.split(' ')
  		intersection=list(set(lines_clean).intersection(set(user_item)))
  		lenth_intersection=len(intersection)
  		difference=list(set(lines_clean).difference(set(user_item)))
  		lenth_difference=len(difference)
  		if lenth_difference!=0:
	  		Similarity=float(lenth_intersection)/lenth_difference
	  		Sim_user.append(Similarity)
	  	else:
	  		Sim_user.append("0")
 	Sim_user_copy=Sim_user[:]
 	Sim_user_copy.sort()
 	Sim_best=Sim_user_copy[-4:]
 	position1=Sim_user.index(Sim_best[3])
 	position2=Sim_user.index(Sim_best[2])
 	position3=Sim_user.index(Sim_best[1])
 	position4=Sim_user.index(Sim_best[0])
 	if position1!=0 and position2!=0 and position3!=0 and position4!=0:
 		recommender=userdic[str(position1)]+" "+userdic[str(position2)]+" "+userdic[str(position3)]+" "+userdic[str(position4)]	
	else:
		recommender="none"
	reco_list=recommender.split(' ')
	recomm=[]
	for good in reco_list:
		if good not in user_item:
			recomm.append(good)
		else:
			pass
	f2.write((" ".join(recomm)+"\n"))
f2.close()
				