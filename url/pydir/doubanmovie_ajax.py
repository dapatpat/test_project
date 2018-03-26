#coding=utf-8
import urllib.request as urllib2
import urllib
url = "https://movie.douban.com/j/new_search_subjects?sort=T&tags=&"

header = {
	"Accept-Language":" zh-Hans-CN,zh-Hans;q=0.5",
	"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
	"Accept":" application/json, text/plain, */*",
	"Host":" movie.douban.com",
	"Connection":" Keep-Alive"
}


formatdata = {
	"sort":"T",
	"range":"0,5",
	"tags":"",
	"start":"10"
}

formatdata = urllib.parse.urlencode(formatdata).encode(encoding="utf-8")
print (formatdata)
request = urllib2.Request(url=url,headers=header,data=formatdata)
douban = urllib2.urlopen(request)

print (douban.read().decode(encoding="utf-8"))