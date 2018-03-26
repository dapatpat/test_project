# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	#公司名
	company_name = scrapy.Field()
	#职位
	job_name = scrapy.Field()
	#工资
	wages = scrapy.Field()
	#工作地点
	local = scrapy.Field()
	#发布日期
	push_date = scrapy.Field()
	#工作经验
	experience = scrapy.Field()
	#学历
	education = scrapy.Field()
	#招聘人数
	recruit = scrapy.Field()
	#招聘人数
	quantity = scrapy.Field()
	#工作要求
	require = scrapy.Field()


