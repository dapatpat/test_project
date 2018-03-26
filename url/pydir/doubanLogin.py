#coding: utf-8
import urllib.request as urllib2
import urllib
from bs4 import BeautifulSoup
from pytesseract import *
from PIL import Image
import os
import http.cookiejar as cookielib


class spider(object):
	def __init__(self):
		self.header =  {'Host':' www.douban.com',
						'Origin':' https://www.douban.com',
						'Connection':' keep-alive',
						'Cache-Control':' max-age=0',
						'Upgrade-Insecure-Requests':' 1',
						'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
						'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
						'Referer':' https://www.douban.com',
						'Accept-Language':' zh-CN,zh;q=0.9'
						# 'Cookie':' bid=mxw3xz1RcPQ; ll="118281"; _vwo_uuid_v2=D538F308B7706F445532F544C132576AC|d909c98ff07e3de470b5a694434e689a; viewed="10773324"; gr_user_id=4f043c6b-6461-4dd6-8e21-caf7e9f96299; __utmc=30149280; __utmz=30149280.1520745351.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.1025380340.1519638697; _gid=GA1.2.1425923480.1520745356; ps=y; ue="are.gum@gmail.com"; push_doumail_num=0; __utmv=30149280.442; ap=1; push_noty_num=0; __utma=30149280.1025380340.1519638697.1520745351.1520755055.4; dbcl2="4426228:OdwxCBl2AEI"; ck=aXfr; __utmb=30149280.19.10.1520755055'
						}			


		self.url = 'https://www.douban.com/accounts/login'
		cookiejar = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar)) 
		urllib2.install_opener(opener)

	def getIndex(self):
		self.html = urllib2.urlopen(urllib2.Request(headers=self.header,url="https://www.douban.com/")).read().decode("utf8")


	def getPage(self):
		html = urllib2.urlopen(urllib2.Request(headers=self.header,url=self.url,data=self.data)).read().decode("utf8")
		with open("./mydouban.html","w") as file:
			file.write(html)
			print("html文件已保存")


	def getCaptimg(self):
		self.soup = BeautifulSoup(self.html,"lxml")
		cap = self.soup.find_all(id="captcha_image")
		capUrl = cap[0].attrs['src']
		Id = self.soup.select("input[name='captcha-id']")
		self.capId = Id[0].attrs['value']
		print ("图片id:"+self.capId)
		# ck = self.soup.select("input[name='ck']")
		# print(ck[0])
		# print("ck:"+self.ck)
		print ("验证码的URL是:"+capUrl)
		capImg = urllib2.urlopen(urllib2.Request(headers=self.header,url=capUrl)).read()
		with open("./capDouban.jpg","wb") as cap:
			cap.write(capImg)
			print ("图片保存完毕")

	def getCaptcha(self):
		# captImage = Image.open("./capDouban.jpg")
		# text = pytesseract.image_to_string(captImage)
		# print ("本次获取到的验证码是:"+text)

		self.captcha = input("请查看验证码图片(capDouban.jpg)然后输入验证码:")
		self.data = {
					# "ck":self.ck,
					"source":"index_nav",
					"redir":'https://www.douban.com',
					"form_email":"are.gum@gmail.com",
					"form_password":"lizhigan2357",
					"captcha-solution":self.captcha,
					"captcha-id":self.capId
					# "login":"登录"
					}
		self.data =  urllib.parse.urlencode(self.data).encode(encoding="UTF8")




def main():
	n=1
	while True:
		try:
			douban = spider()
			# page = douban.getPage()
			douban.getIndex()
			douban.getCaptimg()
			douban.getCaptcha()
			douban.getPage()
			print("执行成功")
			break
		except Exception as e:
			print("第%d次执行失败,重新执行"%1)
			raise e
			break
			

if __name__ == '__main__':
	main()