# #coding: utf-8
import urllib.request as urllib2
from lxml import etree
import json

# headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
# url = "https://tieba.baidu.com/f?kw=2012&ie=utf-8&pn="+str(1*50)
# page = urllib2.urlopen((urllib2.Request(url=url,headers= headers))).read().decode("utf-8")
# html = etree.HTML(page)
# basepath = '//div[@class="t_con cleafix"]'
# titlelist = '//div[@class="t_con cleafix"]//a[contains(@class,"j_th_tit")]/@title'
# hreflist = '//div[@class="t_con cleafix"]//a[contains(@class,"j_th_tit")]/@href'
# authorlist = '//div[@class="t_con cleafix"]//span[contains(@title,"主题作者:")]/@title'
# simple_imglist = '//div[@class="t_con cleafix"]/a//img[contains(@class,"threadlist_pic")]/@src'
# answerlist = '//div[@class="t_con cleafix"]//span[@title="回复"]'
# base = html.xpath(basepath)
# titlelist = './/div[2]/div[1]/div[1]/a/@title'
# hreflist = './/div[2]/div[1]/div[1]/a[@rel="noreferrer"]/@href'
# authorlist = './/div[2]/div[1]/div[2]/span[1]/@title'
# simple_imglist = './/div[@class="small_list_gallery"]//li/a/img/@data-original'
# answerlist = './/div[1]/span[@title="回复"]'

# for i in base:	
# 	print(i)

# 	title = i.xpath(titlelist)[0]
# 	href = i.xpath(hreflist)[0]
# 	author = i.xpath(authorlist)[0]
# 	simple_img = i.xpath(simple_imglist)
# 	print(simple_img)
# 	answer = i.xpath(answerlist)[0].text
# 	print(answer)

# 	infos = {"缩略图连接":simple_img,"标题:":title,"帖子连接":href,"作者:":author,"回复数:":answer}
# 	with open("./tieInfos.txt","a") as infosfile:
# 		# print(1)
# 		infosfile.write(json.dumps(infos,ensure_ascii = False)+"\n\n\n\n")
# 		# print(2)

# print (url)


header = {	"Host":' www.douban.com',
			"Connection":' keep-alive',
			"Cache-Control":' max-age=0',
			"Upgrade-Insecure-Requests":' 1',
			"User-Agent":' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
			"Accept":' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			"Referer":' https://www.douban.com/',
			"Accept-Language":' zh-CN,zh;q=0.9',
			"Cookie":' bid=mxw3xz1RcPQ; ll="118281"; _vwo_uuid_v2=D538F308B7706F445532F544C132576AC|d909c98ff07e3de470b5a694434e689a; viewed="10773324"; gr_user_id=4f043c6b-6461-4dd6-8e21-caf7e9f96299; __utmc=30149280; __utmz=30149280.1520745351.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.1025380340.1519638697; _gid=GA1.2.1425923480.1520745356; ps=y; ue="are.gum@gmail.com"; __yadk_uid=HfNF2eWZ9DMuD7QdRSC6t5Uj7RoLu4gK; push_doumail_num=0; __utmv=30149280.442; ap=1; push_noty_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1520755052%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D1BO_4ectNBsIvP0qBLFBoEyVewLtU9GZSNqE6NlR2MfmGxnzbHU2B5GxyIgAvJ3i%26wd%3D%26eqid%3De20fb9990007bad5000000065aa4bb7c%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1025380340.1519638697.1520745351.1520755055.4; dbcl2="4426228:9qLEQaS/ZcA"; ck=RWtG; _pk_id.100001.8cb4=c31d2a145217888a.1520745348.2.1520759119.1520747985.; __utmb=30149280.13.10.1520755055'
			}
request = urllib2.Request(headers=header,url="https://www.douban.com")
page = urllib2.urlopen(request).read().decode("utf8")
with open("./test.html","w") as file:
	file.write(page)
	