   # -*- coding: UTF-8-*-
import string
import numpy
import pylab

def getstr(word, count):
    countstr = word + ',' + str(count)
    return countstr

def get_wordlist(myfile):
    c = open(myfile).readlines()
    wordlist = []
    for line in c:
        if len(line)>1:
            words = line.split(' ')
            for word in words:
                if len(word)>1:
                    wordlist.append(word).decode('UTF-8')
    return wordlist
    
def get_wordcount(wordlist, outfile):
    out = open(outfile, 'w')
    wordcnt ={}
    for i in wordlist:
        if i in wordcnt:
            wordcnt[i] += 1
        else:
            wordcnt[i] = 1
    worddict = wordcnt.items()
    worddict.sort(key=lambda a: -a[1])
    for word,cnt in worddict:
        out.write(getstr(word.encode('utf-8'), cnt)+'\n')
    out.close()
    return wordcnt

def barGraph(wcDict):
    wordlist=[]
    for key,val in wcDict.items():
        if val>5 and len(key)>3:
            wordlist.append((key.decode('utf-8'),val))
    wordlist.sort()
    keylist=[key for key,val in wordlist]
    vallist=[val for key,val in wordlist]
    barwidth=0.5
    xVal=numpy.arange(len(keylist))
    pylab.xticks(xVal+barwidth/2.0,keylist,rotation=45)
    pylab.bar(xVal,vallist,width=barwidth,color='y')
    pylab.title(u'微博词频分析图')
    pylab.show()
     
if __name__ == '__main__':
    myfile = '/home/alber/data_base/chinese.dat'
    outfile = '/home/alber/data_base/chinese_result.dat'
    wordlist = get_wordlist(myfile)
    wordcnt = get_wordcount(wordlist,outfile)
    barGraph(wordcnt)