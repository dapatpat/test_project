# -*- coding: utf-8 -*-
import scrapy
from txjob import items

class TxjoblistSpider(scrapy.Spider):
	name = 'txjobList'
	allowed_domains = ['hr.tencent.com']
	pn = 0
	count = 1
	start_urls = ['https://hr.tencent.com/position.php?&start='+ str(pn)]

	def parse(self, response):
		# print(response.body.decode("utf8"))
		node = response.xpath('//*[starts-with(@class,"odd") or starts-with(@class,"even")]')
		for each in node:
			try:
				job = items.TxjobItem()
				job["jobName"] = each.xpath('./td[1]/a/text()').extract()[0].strip()
				job["jobType"] = each.xpath('./td[2]/text()').extract()[0].strip()
				job["quantity"] = each.xpath('./td[3]/text()').extract()[0].strip()
				job["address"] = each.xpath('./td[4]/text()').extract()[0].strip()
				job["date"] = each.xpath('./td[5]/text()').extract()[0].strip()
				job["jobHref"] = each.xpath('./td[1]/a/@href').extract()[0].strip()
				job["jobCount"] = "第%d条纪录."%TxjoblistSpider.count
				TxjoblistSpider.count+=1
			except:
				print("在爬取第%d个页面的时候报错."%(TxjoblistSpider.pn+1))
				continue
			print ("链接:"+"https://hr.tencent.com/"+job['jobHref']+"\n")
			yield scrapy.Request("https://hr.tencent.com/"+job['jobHref'],meta={"job":job},callback=self.getDetail)
			
		TxjoblistSpider.pn += 1
		if (TxjoblistSpider.pn-1)*10<= 3800:
			yield scrapy.Request('https://hr.tencent.com/position.php?&start='+ str((TxjoblistSpider.pn-1)*10),callback=self.parse)
			print("已处理完第%d页"%(TxjoblistSpider.pn))
		else:
			print("已爬完%d页"%(TxjoblistSpider.pn))

	def getDetail(self,response):
		job = response.meta["job"]
		node1 = response.xpath('//tr[@class="c"][1]/td[@colspan=3][1]')
		node2 = response.xpath('//tr[@class="c"][2]/td[@colspan=3][1]')
		li1 = node1.xpath('.//li/text()').extract()
		li2 = node2.xpath('.//li/text()').extract()
		content1 = "工作职责:"+"\t"+' '.join(li1)
		content2 = "工作要求:"+"\t"+' '.join(li2)
		content = content1+content2
		# print("拼接结果:"+content)
		job["jobDetail"] = content

		# print ("职位名称:"+job['jobName'])
		# print ("职位类型:"+job['jobType'])
		# print ("招聘人数:"+job['quantity'])
		# print ("工作地址:"+job['address'])
		# print ("发布时间:"+job['date'])
		# print ("工作详情:"+job['jobDetail'])
		print("计数器:%d"%TxjoblistSpider.count)
		yield job