import urllib.request
import os

def download_file():
    folder_path='C:/Users/Administrator/Desktop/download_ooxx'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    os.chdir(folder_path)
    page_number=0
    url='http://www.mzitu.com/'
    for i in range(10):
        page_number+=1
        page_url=url+'page/'+str(page_number)
        img_list=find_imgs(page_url)
        save_imgs(page_url,img_list)

def url_open(url):
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    req=urllib.request.Request(url,None,head)
    response=urllib.request.urlopen(req)
    html=response.read()
    return html
    
def find_imgs(url):
    html=url_open(url).decode('UTF-8')
    img_list=[]
    a=html.find('src=')
    while a!=-1:
        b=html.find('.jpg',a,a+255)
        if b!=-1:
            img_list.append(html[a+5:b+4])
        else:
            b=a+9
        a=html.find('src=',b)
    return img_list

def save_imgs(url,img_list):
    for each in img_list:
        #得到最后一个/后的内容
        imgname=each.split('/')[-1]
        with open(imgname,'wb') as f:
            img=url_open(each)
            f.write(img)

if __name__=='__main__':
    download_file()
