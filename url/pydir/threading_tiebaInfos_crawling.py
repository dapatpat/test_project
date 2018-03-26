#coding: utf-8
from queue import Queue
import  threading
import urllib.request as urllib2
from lxml import etree
import json
from time import sleep

class crawlThread(threading.Thread):
	"""从队列获取url并解析成html的线程"""
	def __init__(self, pageQueue,dataQueue,threadName):
	    super(crawlThread, self).__init__()
	    self.pageQueue = pageQueue
	    self.dataQueue = dataQueue
	    self.name = threadName
	    self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

	def run(self):
		print(self.name+"正在运行")
		global pageLock
		global crawlThreadSwitch
		while crawlThreadSwitch == True:			
			try:
				page = self.pageQueue.get(False)
				url = "https://tieba.baidu.com/f?kw=%E9%98%BF%E6%A3%AE%E7%BA%B3&ie=utf-8&pn="+str(page*50)
				html = urllib2.urlopen((urllib2.Request(url=url,headers= self.headers))).read()
				self.dataQueue.put(html)			
				print ("已获取该页面数据↓↓↓\n"+url)
			except Exception as e:
				pass

		print ("线程"+self.name+"已退出")

class parseThread(threading.Thread):
	"""从html队列获取html并使用lxml从每个队列成员筛选出需要数据的进程"""
	def __init__(self,dataQueue,threadName):
		super(parseThread,self).__init__()
		self.dataQueue = dataQueue
		self.name = threadName

	def parse(self,page):
		print(self.name+"开始解析数据")
		html = etree.HTML(page)
		basepath = '//div[@class="t_con cleafix"]'
		titlelist = '//div[@class="t_con cleafix"]//a[contains(@class,"j_th_tit")]/@title'
		hreflist = '//div[@class="t_con cleafix"]//a[contains(@class,"j_th_tit")]/@href'
		authorlist = '//div[@class="t_con cleafix"]//span[contains(@title,"主题作者:")]/@title'
		simple_imglist = '//div[@class="t_con cleafix"]/a//img[contains(@class,"threadlist_pic")]/@src'
		answerlist = '//div[@class="t_con cleafix"]//span[@title="回复"]'
		base = html.xpath(basepath)
		titlelist = './/div[2]/div[1]/div[1]/a/@title'
		hreflist = './/div[2]/div[1]/div[1]/a[@rel="noreferrer"]/@href'
		authorlist = './/div[2]/div[1]/div[2]/span[1]/@title'
		simple_imglist = './/div[@class="small_list_gallery"]//li/a/img/@data-original'
		answerlist = './/div[1]/span[@title="回复"]'

		for i in base:	
			print(i)
			title = i.xpath(titlelist)[0]
			href = i.xpath(hreflist)[0]
			author = i.xpath(authorlist)[0]
			simple_img = i.xpath(simple_imglist)
			print(simple_img)
			answer = i.xpath(answerlist)[0].text
			print(answer)

			infos = {"缩略图连接":simple_img,"标题:":title,"帖子连接":href,"作者:":author,"回复数:":answer}
			dataLock.acquire()
			print("文件上锁")
			with open("./tieInfos.txt","a") as infosfile:
				# print(1)
				infosfile.write(json.dumps(infos,ensure_ascii = False)+"\n\n\n\n")
				# print(2)
			print (self.name+"已解析并保存数据")
			print("文件解锁")
			dataLock.release()



	def run(self):
		global dataLock
		global parseThreadSwitch
		print(self.name+"正在运行")
		global sum
		while parseThreadSwitch == True:			
			try:
				# print(1)
				html = self.dataQueue.get(False)
				self.parse(html)	
				sum+=1			
				print("已处理第%d个页面"%sum)
			except Exception as e:
				pass

		print ("线程"+self.name+"已退出")

def main():
	pageQueue = Queue()
	dataQueue = Queue()
	crawlName = []
	parseName = []
	clist = []
	plist = []

	global  crawlThreadSwitch
	global  parseThreadSwitch

	for threadName in range(1,4):
		crawlName.append("html获取线程"+str(threadName))
		parseName.append("html页面解析线程"+str(threadName))

	for i in range(0,100):
		pageQueue.put(i)

	for eachThread in crawlName:
		crawl = crawlThread(pageQueue,dataQueue,eachThread)
		clist.append(crawl)
		crawl.start()

	for eachThread in parseName:
		parse = parseThread(dataQueue,eachThread)
		plist.append(parse)
		parse.start()

	sleep(2)

	while True:
		if dataQueue.empty():
			print("dataQueue队列已空")
			if pageQueue.empty():				
				crawlThreadSwitch = False
				parseThreadSwitch = False
				print("全部任务都完程了, 马上退出所有线程")
				break
				# print("pageQueue队列已空,关闭其线程")
			else:
				# print("pageQueue队列仍有%d个任务,先睡0.2秒"%(pageQueue.qsize()))
				sleep(0.2)
		else:
			print ("dataQueue仍有%d个任务在执行中"%dataQueue.qsize())
			if pageQueue.empty():
				print("pageQueue队列已空,关闭其线程")
				crawlThreadSwitch = False

	for item in clist:
		item.join()
		print("退出一个craw线程")
	for item in plist:
		item.join()
		print("退出一个parse线程")


if __name__ == '__main__':
	crawlThreadSwitch = True
	parseThreadSwitch = True
	sum = 0
	sumLock = threading.Lock()
	pageLock = threading.Lock()
	dataLock = threading.Lock()
	main()
	print("已处理%d个页面"%sum)
	print("主线程退出")


