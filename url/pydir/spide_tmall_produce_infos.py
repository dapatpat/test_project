#coding: utf-8
import urllib.request as urllib2
import json
import jsonpath
import urllib
import ssl
from lxml import etree


context = ssl._create_unverified_context()
keyword = input("请输入您要搜索的商品的关键字:")

keyword = urllib.parse.quote(keyword)
url = "https://list.tmall.com/search_product.htm?&q="+keyword+"&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton"
print("url:"+url)
header = {"Host":" list.tmall.com",
"Connection":" keep-alive",
"Upgrade-Insecure-Requests":" 1",
"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Language":" zh-CN,zh;q=0.9",
"Cookie":" cna=A7OFEmvGDAMCAX1eyDJdlBJF; _med=dw:1366&dh:768&pw:1366&ph:768&ist:0; cq=ccp%3D1; hng=; uss=; _m_h5_tk=6b6be91e147678c343c5915ff7bd4943_1519651039993; _m_h5_tk_enc=a35b8e28576c3f4ac72c47c1d3b72704; t=a7de51d482b2e3efc81f4f5bad9b42a6; uc3=nk2=0v4aFzxohHE%3D&id2=UoTYM8HA8kHH&vt3=F8dBz4TUfMzkO1vMtME%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu88AB%5Cu76D6%5Cu5E3D%5Cu738B; lgc=%5Cu88AB%5Cu76D6%5Cu5E3D%5Cu738B; _tb_token_=7741eeeeb3337; cookie2=10709f181d466304fbb1a8c4de370dbf; enc=8DzyLnrSDTxYg2Z4MXmOt5avtF0Cfgx%2B7wCQuTdzvBF9NaNGk0Vcz1YGjM1yl5XR0qTW7l1KzDlu%2FLF52JbNgg%3D%3D; res=scroll%3A1349*6148-client%3A1349*637-offset%3A1349*6148-screen%3A1366*768; pnm_cku822=098%23E1hvspvUvbpvUvCkvvvvvjiPPLcw1jEHRL5ZsjrCPmPZQjYPRFLy0jrnPsSU6j3niQhvCvvv9UUtvpvhvvvvvvGCvvpvvPMMvphvC9vhvvCvpbyCvm9vvvvvphvvvvvv9krvpvFlvvmm86Cv2vvvvUUdphvUOQvv9krvpv3Fuphvmvvv9bm7sfQQkphvC99vvOC0p9yCvhQW139vC0Erzjc6VBi1cXxrlj7Jymx%2FQj7QiXTAVAtlMWLveErtpGLvsnQXHFXXiXVvQE01Ux8x9nFIRfU6pwet9E7r5C69D7zyaXZB; isg=BG9vN-pOaXNYw24ktBKS4tqL_oNzFBk0Wh8VvYH8JV7y0I_SieRThm3BVsBuqJuu"
}


data = {
		"name":"tbuad",
		"ismall":"1",
		"o":"j",
		"pid":"419108_1006",
		"count":"5",
		"keyword":keyword,
		"p4p":"tbcc_p4p_c2016_8_131194_15196411716681519641172163",
		"sbid":"1"	
	}

data = urllib.parse.urlencode(data).encode(encoding="GB2312")

respond = urllib2.Request(url=url,headers=header)
page = urllib2.urlopen(respond,context=context).read().decode("GB2312")

html = etree.HTML(page)
product = "//div[@class='product-iWrap']"
price = product+"//em/@title"
produce_name = product+"//p[contains(@class,'productTitle')]/a/@title"
shop_name = product+"//div[@class='productShop']/a[1]"
chengjiao = product +'//p[@class="productStatus"]//em'
pingjia = product+'//p[@class="productStatus"]/span[a!="旺旺在线"]/a'
print("chengjiao:"+chengjiao)
print("pingjia:"+pingjia)
print("shop_name:"+shop_name)
print("produce_name:"+produce_name)


price_list = html.xpath(price)
product_name_list = html.xpath(produce_name)
shop_name_list = html.xpath(shop_name)
chengjiao_list = html.xpath(chengjiao)
pingjia_list = html.xpath(pingjia)

for x in range(0,len(price_list)):
	print ("姓名:"+product_name_list[x])
	print ("店铺:"+shop_name_list[x].text)
	print ("价格:"+price_list[x])
	print ("成交量:"+chengjiao_list[x].text)
	# print ("评价数:"+pingjia_list[x].text)
	print ("-"*50)

