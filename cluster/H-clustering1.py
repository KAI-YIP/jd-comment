# -*- coding: UTF-8-*-
import numpy as np

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
		for i in samilar_set:
			samilar_list.append(i)
		return samilar_list,len(samilar_list)

	def joincluster(target_joincluster_dict):
		"""对数据集扫描并且合并最相似的两个簇（两者尽量相似而与其他簇尽可能不相似）"""
		
		def makesamilardict(joincluster_dict):
			"""构造簇－簇之间的相似性词典"""
			samilar_dict={}
			name=[]
			joincluster_dict_copy=joincluster_dict.copy()
			for key in joincluster_dict:
				for name in joincluster_dict_copy:
					if key!=name:
						samilar_list,lenth=Hclustering.samilarity(joincluster_dict[key],joincluster_dict[name])
						new_name=tuple([key,name])
						samilar_dict[new_name]=lenth
						name=[]
					else:
						pass
			return samilar_dict

		def makenewcluster(makenewcluster_dict,joincluster_dict):
			"""根据相似性词典，生成新的簇"""
			name_list=[]
			value_list=[]
			joincluster_dict_copy=joincluster_dict.copy()
			for key in makenewcluster_dict:
				value_list.append(makenewcluster_dict[key])
			largest_samilar=max(value_list)
			for key in makenewcluster_dict:
				if makenewcluster_dict[key]==largest_samilar:
					name_list.append(key)
			used_name=[]
			cluster_name=[]
			for name in name_list:
				if name[0] not in used_name and name[1] not in used_name:
					used_name.append(name[0])
					used_name.append(name[1])
					cluster_name.append(name)
				else:
					pass
			for name in cluster_name:
				joincluster_dict_copy[name[0]]+=joincluster_dict_copy[name[1]]
				del joincluster_dict_copy[name[1]]
			return joincluster_dict_copy

		newdict=makesamilardict(target_joincluster_dict)
		newcluster=makenewcluster(newdict,target_joincluster_dict)
		return newcluster

	def savefile(savefile_dict,save_trace='./tplink/test_result1.txt'):
		"""保存新的簇到txt"""
		f=open(save_trace,'a')
		for key in savefile_dict:
			count=0
			f.write(key+" ")
			for word in savefile_dict[key]:
				if count==10:
					count=0
					f.write("     ")
				f.write(word+" ")
				count+=1
			f.write("\n")

if __name__ == '__main__':
	for i in list(range(30)):
		trace_open="./tplink/test/test_result"+str(i)+".txt"
		trace_save="./tplink/test/test_result"+str(i+1)+".txt"
		f=open(trace_open,'r')
		dataset=f.readlines()
		f.close()
		data={}
		count=0
		for line in dataset:
			count+=1
			line_clean=line.split()
			data[count]=line_clean
		secend_cluster=Hclustering.joincluster(data)
		Hclustering.savefile(secend_cluster,trace_save)
