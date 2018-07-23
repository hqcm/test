import time
from urllib import request
import os
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def parsePage(html):
    html = etree.HTML(html)
    img_urls = html.xpath('//div[@class="text"]//img/@src')
    print (img_urls)
    for img_url in img_urls:
        if 'jpg' in img_url:
            name = img_url.split('/')[-1]
            request.urlretrieve(img_url,name)


def getPage(base_url):
    # 第一页请求，并解析
    driver.get(base_url)
    #time.sleep(1)
    html = driver.page_source
    parsePage(html)
    i=2
    while i:
        i-=1
        # 找到下一页按钮
        # 点击搜索按钮
        driver.find_element_by_xpath('//a[@title="Older Comments"]').click()
        time.sleep(1.5)
        html = driver.page_source
        parsePage(html)
        if 'pager_next_disabled' in html:
            break

if __name__ == '__main__':
    # 生成一个浏览器
    options = Options()
    options.add_argument('-headless')  # 无头参数
    driver=webdriver.Firefox(executable_path=r'D:\Program Files (x86)\Mozilla Firefox\geckodriver',firefox_options=options)
    # 通过浏览器发起一个请求
    base_url = 'http://jandan.net/ooxx/page-37#comments'
    folder_path=r'C:\Users\Administrator\Desktop\download_ooxx'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    os.chdir(folder_path)
    getPage(base_url)
    driver.quit()
 
