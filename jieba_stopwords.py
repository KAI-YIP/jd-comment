#coding:utf-8
import jieba  
import jieba.posseg as pseg 
import time  
t1=time.time() 

f1=open("/home/alber/data_base/jd_content/app-mac/mac-result-noflag.txt","r") #读取文本  
segs=f1.read().decode('utf-8')
stopwords_delete=[]
stopwords = {}.fromkeys([ line.rstrip() for line in open('/home/alber/jieba/stopwords.txt') ])  #
for seg in segs:
	seg=str(seg.encode('utf-8'))
	if seg not in stopwords:
		stopwords_delete+=seg
f2=open("/home/alber/data_base/jd_content/app-mac/mac-result.txt","a")
f2.write(stopwords_delete)
f1.close()
f2.close()
t2=time.time() 
print("delete stopwords，耗时："+str(t2-t1)+"秒。") #反馈结果
