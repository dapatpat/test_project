# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhilian.items import ZhilianItem

class ZhaopinSpider(CrawlSpider):
	name = 'zhaopin'
	allowed_domains = ['zhaopin.com']
	#pn是页数 默认先爬取第一页
	pn = 1
	start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=python&isadv=0&sg=7269ff10364f432988975b2c3cccabe4&p='+str(pn)]
	
	#爬取深度为两层:joblink为指向职位详情页数据 pagelikn为总览翻页数据
	joblink = LinkExtractor(allow=(r"jobs.zhaopin.com/\d+.htm"))
	pagelink = LinkExtractor(allow=(r"7269ff10364f432988975b2c3cccabe4&p=\d+"))

	#只翻页  不从职位详情页定向到其他页面  防止数据重复爬取
	rules = (
		Rule(joblink, callback='parse_item', follow=False),#职位详情请求
		Rule(pagelink, follow=True),#翻页请求
	)

	def parse_item(self, response):
		
		job = ZhilianItem()
		node = response.xpath('//div[@class="terminalpage-left"]')

		#公司名
		job["company_name"] = response.xpath('//div[@class="fixed-inner-box"]//h2/a/text()').extract()[0].strip()
		#职位
		job["job_name"] = response.xpath('//div[contains(@class,"f")]/h1/text()').extract()[0].strip()
		#工资
		job["wages"] = node.xpath('.//li[1]/strong/text()').extract()[0].strip()
		#工作地点
		fulllocal = node.xpath('.//li[2]')
		job["local"] = fulllocal.xpath('string(.)').extract()[0].strip()
		#发布日期
		job["push_date"] = node.xpath('.//li[3]/strong//text()').extract()[0].strip()
		#工作经验
		job["experience"] = node.xpath('.//li[5]/strong/text()').extract()[0].strip()
		#学历
		job["education"] = node.xpath('.//li[6]/strong/text()').extract()[0].strip()
		#招聘人数
		job["quantity"] = node.xpath('.//li[7]/strong/text()').extract()[0].strip()
		#工作要求:因为都是同级的P标签  所以先把该node下面的全部P标签匹配出来 再把末尾的信息进行切片
		rlist = node.xpath('.//div[@class="tab-inner-cont"][1]/p/text()').extract()[:-4]
		job["require"] = " ".join(rlist)

		# print ("公司名:"+job["company_name"])
		# print ("职位:"+job["job_name"])
		# print ("工资:"+job["wages"])
		# print ("工作地点:"+job["local"])
		# print ("发布日期:"+job["push_date"])
		# print ("工作经验:"+job["experience"])
		# print ("学历:"+job["education"])
		# print ("招聘人数:"+job["quantity"])
		# print ("工作要求:"+job["require"])

		return job