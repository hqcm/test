import urllib.request
import re

def download_file():
    url='http://jandan.net/ooxx'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req=urllib.request.Request(url,None,head)
    response=urllib.request.urlopen(req)
    html=response.read().decode()
    number=re.findall(r'<span class="current-comment-page">\[(\d\d)\]</span>', html)[0]
    print (number)
    
if __name__=='__main__':
    download_file()
