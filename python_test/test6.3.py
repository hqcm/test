import urllib.request
import urllib.parse
import json
import time
while True:
    content=input('请输入所要翻译的内容（输入q退出程序）：')
    if content=='q':
        break
    url='http://fanyi.youdao.com/translate'
    data={'i':content,'type':'AUTO','doctype':'json','version':'2.1','keyfrom':'fanyi.web','ue':'UTF-8','typoResult':'true'}
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    data=urllib.parse.urlencode(data).encode('UTF-8')
    #在包含head信息时采用此函数
    req=urllib.request.Request(url,data,head) 
    response=urllib.request.urlopen(req)
    html=response.read().decode('UTF-8')
    target=json.loads(html)
    print('翻译结果为:%s' %(target['translateResult'][0][0]['tgt']))
    time.sleep(1)
 
