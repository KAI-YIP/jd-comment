# -*- coding: UTF-8-*-
import numpy as np
import numpy as np
import os,shutil,sys

class Hclustering:
	"""层次聚类算法"""

	def openfile(openfile_trace="./tplink/test.txt"):
		"""打开文件，提取为字典"""
		f=open(openfile_trace,'r')
		dataset=f.readlines()
		f.close()
		data={}
		for line in dataset:
			line_clean=line.split()
			data[line_clean[0]]=line_clean[1:]
		return data

	def samilarity(samilarity_list1,samilarity_list2):
		"""两向量的相似性"""
		samilar_list=[]
		samilar_set=set(samilarity_list2)&set(samilarity_list1)
		a=len(samilarity_list1)+len(samilarity_list2)-len(samilar_set)
		for i in samilar_set:
			samilar_list.append(i)
		return samilar_list,len(samilar_list)/a

	def joincluster(target_joincluster_dict,joincluster_threshold=0.4):
		"""对数据集扫描并且合并最相似的两个簇（两者尽量相似而与其他簇尽可能不相似）"""
		
		def makesamilardict(joincluster_dict):
			"""构造簇－簇之间的相似性词典"""
			samilar_dict={}
			name=[]
			joincluster_dict_copy=joincluster_dict.copy()
			for key in joincluster_dict:
				for name in joincluster_dict_copy:
					if key!=name and (key,name) not in samilar_dict and (name,key) not in samilar_dict:
						samilar_list,lenth=Hclustering.samilarity(joincluster_dict[key],joincluster_dict[name])
						new_name=tuple([key,name])
						samilar_dict[new_name]=lenth
						name=[]
					else:
						pass
			return samilar_dict

		def makenewcluster(makenewcluster_dict,joincluster_dict):
			"""根据相似性词典，生成新的簇"""
			value_list=[]
			joincluster_dict_copy=joincluster_dict.copy()
			for key in makenewcluster_dict:
				value_list.append(makenewcluster_dict[key])
			value_list_set=set(value_list)
			value_list=[]
			new_dict=[]
			for i in value_list_set:
				if i>=joincluster_threshold:
					value_list.append(i)
			new_value_list=sorted(value_list,reverse=True)
			for value in new_value_list:
				for key in makenewcluster_dict:
					if makenewcluster_dict[key]==value:
						if key[0] in joincluster_dict_copy and key[1] in joincluster_dict_copy:
							joincluster_dict_copy[str(key[0])+"+"+str(key[1])]=joincluster_dict[key[0]]+joincluster_dict[key[1]]
							del joincluster_dict_copy[key[0]]
							del joincluster_dict_copy[key[1]]
			return joincluster_dict_copy
							
		newdict=makesamilardict(target_joincluster_dict)
		newcluster=makenewcluster(newdict,target_joincluster_dict)
		return newcluster


	def savefile(savefile_dict,save_trace='./tplink/test_result1.txt'):
		"""保存新的簇到txt"""
		f=open(save_trace,'a')
		for key in savefile_dict:
			f.write(str(key)+" ")
			count=0
			for word in savefile_dict[key]:
				if count==10:                                  #此处设定特征数量
					count=0
					f.write("     ")
				f.write(word+" ")
				count+=1
			f.write("\n")

if __name__ == '__main__':
	lenth=10											#设定簇的数量
	threshold=[0.01,0.05,0.08,0.1,0.12,0.15,0.2]
	for shold in threshold:
		thresholod_trace="相似度阈值"+str(shold)
		os.mkdir("./tplink/h-cluster/"+thresholod_trace)
		shutil.copyfile("./tplink/h-cluster/test_result0.txt","./tplink/h-cluster/"+thresholod_trace+"/test_result0.txt") 
		f3=open("./tplink/h-cluster/"+thresholod_trace+"/topic_tree.txt",'a')
		for i in list(range(30)):
			trace_open="./tplink/h-cluster/"+thresholod_trace+"/test_result"+str(i)+".txt"
			trace_save="./tplink/h-cluster/"+thresholod_trace+"/test_result"+str(i+1)+".txt"
			f=open(trace_open,'r')
			dataset=f.readlines()
			f.close()
			data={}
			for line in dataset:
				line_clean=line.split()
				data[line_clean[0]]=line_clean[1:]
			for key in data:
				f3.write(str(key)+"　　　")
			f3.write("\n")
			second_cluster=Hclustering.joincluster(data,shold)
			f3.write("\n")
			if lenth==len(second_cluster):
				break
			else:
				lenth=len(second_cluster)
			Hclustering.savefile(second_cluster,trace_save)