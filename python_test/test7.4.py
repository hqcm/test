import urllib.request
import re
import os

def download_file():
    folder_path='C:/Users/Administrator/Desktop/download_ooxx'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    os.chdir(folder_path)
    url='https://tieba.baidu.com/p/5621324723'
    find_imgs(url)

def url_open(url):
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req=urllib.request.Request(url,None,head)
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
    
def find_imgs(url):
    html=url_open(url).decode('UTF-8')
    #将一个子组挑出来，即直接得到每张图的地址
    p=r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    img_list=re.findall(p,html)
    for each in img_list:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each,filename,None)

if __name__=='__main__':
    download_file()

#注意filename不要直接以each来命名，会报错，是由于文件的命名中不能包含/等非法字符
 
