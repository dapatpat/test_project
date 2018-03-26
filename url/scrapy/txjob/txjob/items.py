# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TxjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobType = scrapy.Field()
    quantity = scrapy.Field()
    address = scrapy.Field()
    date = scrapy.Field()
    jobHref = scrapy.Field()
    jobDetail = scrapy.Field()
    jobCount = scrapy.Field()