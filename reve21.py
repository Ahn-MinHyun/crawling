from requests.api import request
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from urllib.request import Request, urlopen
import requests

# opener=urllib.request.build_opener()
# opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
# urllib.request.install_opener(opener)

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# print(PROJECT_ROOT)
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
cnt = 1
url = 'https://www.reve21.co.jp/results/'

# proxy = ProxyHandler({'http': 'http://192.168.1.31:8888'})
# urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
# result = urlretrieve(url=file_url, filename=file_name)
# headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
# r=request(headers=headers)
browser = webdriver.Chrome() #usr/bin

browser.get(url)
browser.implicitly_wait(time_to_wait=20)

def url_print(PATH):
    img = browser.find_element_by_xpath(PATH).get_attribute("src")
    return img
    # img = browser.find_element_by_xpath(PATH)
    # before_url = img.value_of_css_property('background-image')
    # before_url = before_url.lstrip('url("').rstrip('")')
    # return before_url

def text_print(PATH):
    info_text = browser.find_element_by_xpath(PATH)
    return info_text.text



for i in range(1,2):# 93+1
    img_url =[] # 0.환자 1.초기상태, 2.초기검사
    info_text= [] # 홀수 초기, 짝수 호전
    print(i)

    # image url
    # try :
    #     before_PATH = '//*[@id="resultBox"]/div['+str(i)+']/a/figure/img[2]'
    #                 # 마지막 데이터 셋
    #                 #    //*[@id="resultBox"]/div[93]/a/figure/img[2]
    #     img_url.append(url_print(before_PATH))
    #     progress_PATH='//*[@id="resultBox"]/div['+str(i)+']/a/figure/img[3]'
    #     img_url.append(url_print(progress_PATH))
    #     after_PATH = '//*[@id="resultBox"]/div['+str(i)+']/a/figure/img[4]'
    #     img_url.append(url_print(after_PATH))
    #     print(img_url)
    # except NoSuchElementException:
    #     print('image NoSuchElementException 패 스')

    #환자정보
    # classi_PATH  = '//*[@id="resultBox"]/div[1]/a/h2/i/font/font'
    # print(text_print(classi_PATH))
    # info_text.append(text_print(classi_PATH))
    
    try :
        # 초기상태 
        info_text_1 = '//*[@id="resultBox"]/div['+str(i)+']/a/h2'
        info_text.append(text_print(info_text_1))
        info_text_2 = '//*[@id="resultBox"]/div['+str(i)+']/a/ul'
        info_text.append(text_print(info_text_1))
    except NoSuchElementException:
        print('text NoSuchElementException 패 스')
    # txt저장

    f = open('./downloads/reve21/'+str(cnt)+".txt", 'w')
    f.write('\n\n'.join(info_text))
    f.close()

    # # # 사진 저장
    # for idx,url in enumerate(img_url):
    # urlretrieve('https://www.reve21.co.jp/assets/img/results/customer_001_before.jpg', f'./downloads/reve21/'+str(cnt)+'-'+ str(1+1) +'.jpg')
    # cnt += 1

browser.close()

# ---------- infomation -----------

# cnt = 1
# last_img = 21+1
# # for page in range(1, 17+1):
# for page in range(1, 17+1):
#     print('page : '+ str(page))
#     url = "https://www.morakmorak.com/before_after/page/"+str(page)+"/"

#     browser = webdriver.Chrome() #usr/bin

#     browser.get(url)
#     browser.implicitly_wait(time_to_wait=10)
#     if page == 17:
#         last_img = 18+1
#     for i in range(1, last_img):
#         # print(classifi_text.text)
#         info_PATH = '//*[@id="main-wrapper"]/div[2]/div/div/div/div[1]/div['+str(i)+']/a'
#         info_browser = browser.find_element_by_xpath(info_PATH)
#         info_browser.click()
#         classifi_PATH  = '//*[@id="main-wrapper"]/div[2]/div[1]'
#         classifi_text = browser.find_element_by_xpath(classifi_PATH)
#         info_text_1 = '//*[@id="tab-1"]'
#         info_text_1 = browser.find_element_by_xpath(info_text_1)
#         info_text_2 = '//*[@id="tab-2"]'
#         info_text_2 = browser.find_element_by_xpath(info_text_2)

#         # print(info_text_1.text)
#         # print(info_text_2.text)
#         print(classifi_text.text)
#         img_folder = './downloads/morak/'
#         if not os.path.isdir(img_folder) :
#             os.mkdir(img_folder)
#         f = open('./downloads/morak/'+str(cnt)+".txt", 'w')
#         f.write(classifi_text.text+ "\n\n"+info_text_1.text +"\n\n"+ info_text_2.text )
#         f.close()
#         cnt += 2

#         browser.back()

#     browser.close()

