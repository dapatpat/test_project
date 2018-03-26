#coding=utf-8
import urllib.request as urllib2
import random 
import urllib
import chardet
#注册为u


#构造useragen列表并随机选择一个
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]
user_agent = {"User-Agent":random.choice(ua_list)}

url = input("请输入你要查询的页面地址:")
url = "http://"+url+"/f?"+"&ie=utf-8"
keyword = input("请输入贴吧名:")
kw = {"kw":keyword}
kw = urllib.parse.urlencode(kw)
fp = int(input("请输入你要爬的起始页码:"))
ep = int(input("请输入你要爬的结尾页码:"))
for pn in range(fp,ep+1):
	fullurl = url+kw+"&pn="+str((pn-1)*50)
	print ("fullurl:"+fullurl)
	request = urllib2.Request(fullurl,headers=user_agent)
	p = urllib2.urlopen(request)
	# page = p.read()
	# print (page.decode("UTF-8"))
	with open("./爬取的页面/%s吧_第%d页.html"%(keyword,pn),"w",encoding="utf-8") as file:
		print ("正在写入第%s页......"%pn)
		file.write(str(p.read().decode("UTF-8")))
	print ("第%s页写入完成."%pn)
# baidu = urllib2.urlopen(request)
# print (baidu.info())
