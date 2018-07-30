from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
options = Options()
options.add_argument('-headless')  # 无头参数
driver=webdriver.Firefox(executable_path=r'D:\Program Files (x86)\Mozilla Firefox\geckodriver',firefox_options=options)
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys("西安")
driver.find_element_by_id("su").click()
driver.save_screenshot(r'C:\Users\Administrator\Desktop\西安.png')
driver.quit()