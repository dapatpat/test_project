# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

# class Myproject1Pipeline(object):
#     def process_item(self, item, spider):
#         return item

class csdnPipeline(object):
	def __init__(self):
		self.filename = open("./csdn.json","w")

	def process_item(self,item,spider):
		print("********")
		jsontext = json.dumps(dict(item),ensure_ascii=False)
		self.filename.write(jsontext+"\n")
		return item

	def close_spider(self,spider):
		print("爬虫关闭")
		self.filename.close()

