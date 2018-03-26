# -*- coding: utf-8 -*-
import scrapy
from myProject1.items import csdnItems


class csdnSpider(scrapy.Spider):
	name = 'csdn'
	allowed_domains = ['https://blog.csdn.net']
	start_urls = ['https://blog.csdn.net/nav/ai']

	def parse(self, response):
		# print(response.body.decode("utf8"))
		items = []
		print ("总长度:"+str(len(response.xpath('//ul[@id="feedlist_id"]/li[@data-type="blog"]'))))
		for each in response.xpath('//ul[@id="feedlist_id"]/li[@data-type="blog"]'):
			# print (each)
			item = csdnItems()
			item["title"] = (each.xpath('.//div/div/h2/a[@strategy="new"]/text()').extract()[0].strip())
			item["autor"] = (each.xpath('.//dd[@class="name"]/a/text()').extract()[0].strip())
			item["reading"] = (each.xpath('.//div/p[@class="num"]/text()').extract()[0].strip())

			items.append(item)
			yield item
		n = 0
		for n in range(0,len(items)):
			print("标题:"+"\t"+items[n]["title"],end="\n")
			print("作者:"+"\t"+items[n]["autor"],end="\n")
			print("阅读量:"+"\t"+items[n]["reading"],end="\n")
			print("\n"*2)
			n+=1

			
