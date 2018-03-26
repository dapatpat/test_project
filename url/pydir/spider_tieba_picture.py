# -*- coding: UTF-8 -*-
import urllib.request as urllib2
import urllib
import re
from lxml import etree

# url = "http://neihanshequ.com/bar/1/"

# <h1 class="title">
# 				<p>反正闲着也是闲着 ，于是买了些饺子皮，肉，韭菜，小葱，生姜回家包饺子吃。包好后我在厨房煮，煮好了端过去给他们吃。一人一碗刚刚好，然后开始下第二锅，刚下没多久呢，小叔子拿着碗进来了，看着他瞄着饺子欲言又止还满脸通红的样子，我灵机一动说了句：天王盖地虎</p>
# 				</h1>

# rule = re.compile(r'<h1 class="title">(.*?)</h1>',re.S)

# request = urllib2.Request(headers = header,url = url)

# html = urllib2.urlopen(request)

# html = str(html.read().decode("utf-8"))

# result = rule.findall(html)

# for x in result:
# 	print(x.strip().replace("<p>","").replace("</p>","")+"\n"+"\n"+"\n")



class spider(object):
	"""爬虫类"""
	def __init__(self):
		pass

	def get_url(self):
		"""获取贴吧名字并拼接成完整url"""
		tieba_name = input("请输入您要爬的贴吧名字:")
		star_pn = int(input("请输入起始页:"))
		# end_pn = input("请输入芥末页:")
		self.url = "https://tieba.baidu.com/f?kw="+tieba_name+"&pn=%d"%((star_pn-1)*50)
		print("url解析完毕, 需要解析的url地址为 :%s"%self.url)

	def open_url(self,url=""):
		"""打开url,返回urlopen对象"""
		header = {
		"Host": "tieba.baidu.com",
		"Connection": "keep-alive",
		"Accept": "*/*",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
		"Accept-Language": "zh-CN,zh;q=0.9"
		}
		print("self.url:%s"%self.url)
		self.open = urllib2.urlopen(urllib2.Request(self.url))
		print("页面加载完毕")

	def make_html(self):
		"""获取html页面"""
		self.html = self.open.read().decode("utf-8")

		
	def handle_html(self):
		xml_page = etree.HTML(self.html)
		# print(type(self.open))
		self.urllist = xml_page.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
		# for e in self.urllist:
		# 	print(e)
		def get_img():
			base_url = "https://tieba.baidu.com"
			filename = 0
			for e in self.urllist:
				img_html = urllib2.urlopen(urllib2.Request(base_url+e)).read().decode("utf-8")
				# print (img_html)
				img_list = etree.HTML(img_html).xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')
				# print (img_list)
				for img in img_list:
					print (filename)
					images = urllib2.urlopen(urllib2.Request(img)).read()
					with open("./image/"+str(filename)+".jpg","wb") as image:
						image.write(images)
						print("图片%s.jpg已保存"%filename)
						filename = filename+1

		# get_url()
		get_img()



def main():
	s = spider()
	s.get_url()
	s.open_url()
	s.make_html()
	s.handle_html()
if __name__ == '__main__':
	main()