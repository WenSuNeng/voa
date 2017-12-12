'''
第一个示例：简单的网页爬虫

爬取voa首页
'''
#import db_init.py
import os,time
import sqlite3
import urllib.request
import re
import re_pattern
con = sqlite3.connect("voa.db")
#网址
url = "http://www.51voa.com"

#def 

#请求
#while True:
#	time.sleep(1)
#	if time.ctime()[12:19]=="8:00:00" or time.ctime()[12:19]=="20:03:00" :
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式
data = data.decode('utf-8')

#打印结果
#print(data)

output = open('read.txt','w')
#output.write(data)

	
#打印爬取网页的各类信息

#print(type(response))
#print(response.geturl())
#print(response.info())
#print(response.getcode())

#打印经过正则表达式过滤后的信息
items = re.findall(re_pattern.pattern,data)
for item in items:
	#print('www.51voa.com/' + item)
	#output.write('\n\nwww.51voa.com/' + item)
	str = 'www.51voa.com/' + item 
	try:
		con.execute("INSERT INTO voa (id, title) VALUES (NULL,  '"+ str +"');")
	except:
		continue

con.commit()

con.close()



