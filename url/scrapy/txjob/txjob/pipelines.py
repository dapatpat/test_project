# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TxjobPipeline(object):
	def __init__(self):
		self.file = open("./txjobList.json","w")

	def process_item(self, item, spider):
		text = json.dumps(dict(item),ensure_ascii=False)+"\n"*3
		self.file.write(text)
		return item

	def close_spider(self,spider):
		self.file.close()
		print("信息已全部爬取并保存,关闭文件.")
