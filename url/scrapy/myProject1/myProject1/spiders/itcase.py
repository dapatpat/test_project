# -*- coding: utf-8 -*-
import scrapy


class ItcaseSpider(scrapy.Spider):
    name = 'itcase'
    allowed_domains = ['itcase.cn']
    start_urls = ['http://www.itcase.cn/channel/teacher.shtml#']

    def parse(self, response):
        with open("./itcase.html","w") as file:
        	file.write(response.body)
