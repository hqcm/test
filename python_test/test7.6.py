import urllib.request
import re
import os
import time

def download_file():
    folder_path='C:/Users/Administrator/Desktop/download_ooxx'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    os.chdir(folder_path)
    url='http://www.xicidaili.com/'
    find_imgs(url)

def url_open(url):
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req=urllib.request.Request(url,None,head)
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
    
def find_imgs(url):
    html=url_open(url).decode('UTF-8')
    p=r'(?:(?:[1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[1]?\d?\d|2[0-4]\d|25[0-5])'
    ip_list=re.findall(p,html)
    for each in ip_list:
        print (each)

if __name__=='__main__':
    download_file()

