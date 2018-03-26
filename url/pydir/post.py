#coding=utf-8
import urllib.request as urllib2
import random 
import urllib
import chardet

#注册为u

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
header = {
	"Host":" fanyi.youdao.com",
	"Accept":" application/json, text/javascript, */*; q:0.01",
	"Origin": "http://fanyi.youdao.com",
	"X-Requested-With":" XMLHttpRequest",
	"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
	"Referer": "http://fanyi.youdao.com/",
	"Accept-Language":"zh-CN,zh;q=0.9"
}

while True:
	word =  input ("请输入你要翻译的单词:")

	formatdata = {
		"i":word,
		"from":"AUTO",
		"to":"AUTO",
		"smartresult":"dict",
		"doctype":"json",
		"version":"2.1",
		"keyfrom":"fanyi.web",
		"action":"FY_BY_CLICKBUTTION",
		"typoResult":"true"
		}
	formatdata = urllib.parse.urlencode(formatdata).encode(encoding="UTF8")
	# print (formatdata)
	request = urllib2.Request(url,data=formatdata, headers=header)
	send = urllib2.urlopen(request)

	result = send.read().decode("utf-8")
	result = (eval(result))
	# print (result)
	result = result["translateResult"][0][0]["tgt"]
	# print (result)
	print ("%s------->%s"%(word,result))
