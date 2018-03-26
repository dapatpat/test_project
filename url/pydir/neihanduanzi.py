#coding=utf-8
import urllib.request as urllib2
import urllib
import re

url = "http://neihanshequ.com/bar/1/"

# <h1 class="title">
# 				<p>反正闲着也是闲着 ，于是买了些饺子皮，肉，韭菜，小葱，生姜回家包饺子吃。包好后我在厨房煮，煮好了端过去给他们吃。一人一碗刚刚好，然后开始下第二锅，刚下没多久呢，小叔子拿着碗进来了，看着他瞄着饺子欲言又止还满脸通红的样子，我灵机一动说了句：天王盖地虎</p>
# 				</h1>
header = {
	"Host":" neihanshequ.com",
	"Connection":" keep-alive",
	"Cache-Control":" max-age=0",
	"Upgrade-Insecure-Requests":" 1",
	"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Language":" zh-CN,zh;q=0.9",
	"Referer":"https://www.baidu.com/link?url=g2cR22i2SLkv5nc_JeBNX7mQBDitBR-7QxRHvWb2m7MnZ2lAKDkqSiJptONdH9r1&wd=&eqid=a199636e0000e4d1000000065a7fff7d"
}

rule = re.compile(r'<h1 class="title">(.*?)</h1>',re.S)

request = urllib2.Request(headers = header,url = url)

html = urllib2.urlopen(request)

html = str(html.read().decode("utf-8"))


result = rule.findall(html)

for x in result:
	print(x.strip().replace("<p>","").replace("</p>","")+"\n"+"\n"+"\n")