# -*- coding: UTF-8-*-

class lda:
	"""主题两两之间的相似，并输出"""

	def f_open_file(file_trace="./lda/iphone5s/diff-sampling/model-1.txt"):
		"""打开模型并保存为字典"""
		f=open(file_trace,'r')
		count=0
		txt=f.readlines()
		f.close()
		topic_dict={}
		topic_unpro_dict={}
		word=[]
		word_value=[]
		for line in txt:
			if "Topic" in line:
				name=line[:-1]
			else:
				line_list=line.split()
				word.append(line_list[0])
				line_clean=" ".join(line_list)
				word_value.append(line_clean)

			if count==word_number:
				topic_dict[name]=word_value
				topic_unpro_dict[name]=word
				count=0
				word=[]
				word_value=[]
			else:
				count+=1
		return topic_dict,topic_unpro_dict

	def f_static_word(static_word_dict,static_word_topicNum=30,static_word_wordNum=50):
		"""统计词并输出"""
		wordlist=[]
		for key in static_word_dict:
			for word in static_word_dict[key]:
				if word not in wordlist:
					wordlist.append(word)
				else:
					pass
		print ("topic数量取(%d),word数量取(%d),无overlap时词数量为(%d),实际词数量为(%d)",static_word_topicNum,static_word_wordNum,static_word_wordNum*static_word_topicNum,len(wordlist))
		return wordlist

	def f_samilarity(samilarity_word_list1,samilarity_word_list2,samilarity_threshold=5):
		intersection=set(samilarity_word_list1)&set(samilarity_word_list2)
		len_intersection=len(intersection)
		if len_intersection>=samilarity_threshold:
			return len_intersection
		else:
			pass

	def f_save_file(save_file_list,save_trace="./lda/iphone5s/diff-sampling/samilar.txt"):
		f=open(save_trace,'a')
		for word in save_file_list:
			word_write=str(word)+"\n"
			f.write(word_write)
		f.close()
		print ("(%s has been saved",save_file_list)


if __name__ == '__main__':
	samilarity=[]
	topic_dict,topic_unpro_dict=lda.f_open_file()
	print (len(lda.f_static_word()))
	for key1 in topic_unpro_dict:
		for key2 in topic_unpro_dict:
			if key2!=key1 and lda.f_samilarity(topic_unpro_dict[key1],topic_unpro_dict[key2],5)==None:
				topic_intersection=key1+" "+key2
				samilarity.append(topic_intersection)
			else:
				pass
	print (len(samilarity))