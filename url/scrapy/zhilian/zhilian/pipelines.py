# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ZhilianPipeline(object):
	def __init__(self):
		self.file = open("./zhilian_job.json","w")


	def process_item(self, item, spider):
		jobInfo = json.dumps(dict(item),ensure_ascii=False)
		print("开始写入文件")
		self.file.write(jobInfo+"\n"*2)
		return item
	
	def close_spider(self,spider):
		self.file.close()
		print("数据已写入,关闭文件")
			