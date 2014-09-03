# -*- coding: UTF-8-*-
from os import listdir
import numpy as np

class ldaCluster:
	"""对LDA的多次实验主题进行k-means聚类"""

	def f_file_namelist(name_index="./tplink/"):
		"""获取某目录下所有文件并将lda主题-词存储为字典"""
		file_list=listdir(name_index)
		topic_dict={}
		topic_dict_nopro={}
		filelist=[]
		name_count=0
		for name in file_list:
			trace=name_index+name
			f=open(trace,'r')
			for line in f.readlines():
				if line[0]!="	":
					word_prob=[]
					word_noprob=[]
					dict_name="topic"+str(name_count)
					name_count+=1
				else:
					line_clean=line.split()
					word_prob.append(line_clean)
					word_noprob.append(line_clean[0])
				topic_dict[dict_name]=word_prob
				topic_dict_nopro[dict_name]=word_noprob
		return topic_dict,topic_dict_nopro

	def f_kmeans(kmeans_topic_dict_nopro,k=4):
		"""设定初始K值，带入计算字典进行k-means聚类"""

		def f_intersection(samilar_list1,samilar_list2):
			"""两文档列列表的相似度(词数量少，直接用交集作为相似度)"""
			samilar_list=[]
			samilar_set=set(samilar_list2)&set(samilar_list1)
			for i in samilar_set:
				samilar_list.append(i)
			return samilar_list,len(samilar_list)

		def f_random_initialdot(kmeans_topic_dict_nopro,k):
			"""从topic集中随机选择K组"""
			random_namelist=[]
			for key in topic_dict_nopro:
				random_namelist.append(key)
			ret=random.sample(random_namelist,k)
			return ret

		def f_cluster(cluster_initial_dot,kmeans_topic_dict_nopro):
			"""依据给定的Ｋ个聚类中心对数据分簇(有可能有空簇)"""
			cluster={}
			for name in cluster_initial_dot:
				cluster[name]=[name]
			for key in kmeans_topic_dict_nopro:
				lenth_ex=0
				if key not in cluster_initial_dot:
					for dot in cluster_initial_dot:
						samilar,lenth_samilar=f_intersection(kmeans_topic_dict_nopro[key],kmeans_topic_dict_nopro[dot])
						if lenth_samilar>lenth_ex:
							lenth_ex=lenth_samilar
							cluster_target=dot
						else:
							pass
					cluster[cluster_target].append(key)
			print (len(cluster))
			return cluster

		def f_find_centroid(kmeans_topic_dict_nopro,find_centroid_cluster):
			"""计算簇的新质点中心"""
			for key in find_centroid_cluster:






if __name__ == '__main__':
	a,b=ldaCluster.f_file_namelist()


