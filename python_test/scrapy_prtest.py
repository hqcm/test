import requests
import re
from lxml import etree
url='http://jandan.net/ooxx'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
html= requests.get(url,headers=headers).content
html=etree.HTML(html)
urls=html.xpath('//span[@class="tucao-like-container"]/span/text()')
print (urls)
