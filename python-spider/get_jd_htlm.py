import urllib2  
import os 
import sys
weburltitle="http://club.jd.com/review/1065978-0-"    #Str before the additional NO. of weburl 
weburltail="-0.html"       #Str after the additional NO. of weburl 
addition=1                     #first value of addition
while addition<=1:      #additional value of addition
   weburl=weburltitle+str(addition)+weburltail
   response = urllib2.urlopen(weburl)  
   html = response.read()  
   jddata=open('/home/alber/dataget/jddata.txt','w')    #save the data into TXT
   jddata.write(html)
   addition=addition+1
   