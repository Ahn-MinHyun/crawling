from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print(PROJECT_ROOT)
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

url = "https://maxwellhair.com/before_after/?page=2"

browser = webdriver.Chrome() #usr/bin

browser.get(url)
browser.implicitly_wait(time_to_wait=20)
# page = str(2)
# page_number = '//*[@id="container-async"]/div/ul/li['+page+']/a'


img_url = []
for i in range(1, 12+1):
    print(i)
    url_PATH = '//*[@id="container-async"]/div/div[1]/div['+str(i)+']/div[1]/div[1]'
    img = browser.find_element_by_xpath(url_PATH)
    bg_url = img.value_of_css_property('background-image')
    bg_url = bg_url.lstrip('url("').rstrip('")')
    after_PATH = '//*[@id="container-async"]/div/div[1]/div['+str(i)+']/div[1]/div[3]'
                #   //*[@id="container-async"]/div/div[1]/div[1]/div[1]/div[3]
                #   //*[@id="container-async"]/div/div[1]/div[12]/div[1]/div[3]
    after_img = browser.find_element_by_xpath(after_PATH)
    after_url = after_img.value_of_css_property('background-image')
    after_url = after_url.lstrip('url("').rstrip('")')
    img_url.append(bg_url)
    img_url.append(after_url)
# print(img_url)
img_folder = './downloads'
if not os.path.isdir(img_folder) :
    os.mkdir(img_folder)
for idx,url in enumerate(img_url):
    urlretrieve(url, f'./downloads/'+str(25+idx)+'.jpg')

browser.close()

