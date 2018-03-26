# -*- coding: UTF-8 -*-
import urllib.request as urllib2
import json
import jsonpath


header = {
	"Accept":" application/json, text/javascript, */*; q:0.01",
	"X-Requested-With":" XMLHttpRequest",
	"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
	"Accept-Language":"zh-CN,zh;q=0.9"
}

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

link = urllib2.Request(url=url,headers=header)
html = urllib2.urlopen(link).read().decode("UTF8")

infos = json.loads(html)
rule = "$content.data.allCitySearchLabels..[*].id"
city_name = jsonpath.jsonpath(infos,"$.content.data.allCitySearchLabels..[*].id")

# print (str(city_name))
for city in city_name:
	print (city,end = "\t")


