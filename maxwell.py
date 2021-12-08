from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException



PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print(PROJECT_ROOT)
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
browser = webdriver.Chrome('/Users/mac/Desktop/bbz/crawling/crawling/chromedriver') # 크롬드라이버 주소
cnt = 1
url = "https://jongno.maxwellhair.com/before_after/"

browser.get(url)
browser.implicitly_wait(time_to_wait=10)

info_PATH = '//*[@id="container-async"]/div/ul/li[2]/a'
info_browser = browser.find_element_by_xpath(info_PATH)

info_browser.click()

# 이미지 주소 가져오는 함수
def url_print(PATH):
    img = browser.find_element_by_xpath(PATH)
    before_url = img.value_of_css_property('background-image')
    before_url = before_url.lstrip('url("').rstrip('")')
    return before_url
    # before_url = img.value_of_css_property('background-image')
    # before_url = before_url.lstrip('url("').rstrip('")')
    # return img 
# 텍스트 가져오는 함수
def text_print(PATH):
    info_text = browser.find_element_by_xpath(PATH)
    return info_text.text


for img_number in range(1,12+1): # 페이지의 이미지 장수
    # 이미지 주소리스트 
    img_url =[] 
    # 텍스트 리스트 
    info_text= [] 

    try :
        before_PATH = '//*[@id="container-async"]/div/div[1]/div['+str(img_number)+']/div[1]/div[1]'
                        # //*[@id="pageJissekiMan"]/div[2]/div[1]/ul/li[2]/div/a[1]/img
        img_url.append(url_print(before_PATH))
        after_PATH= '//*[@id="container-async"]/div/div[1]/div['+str(img_number)+']/div[1]/div[3]'
        img_url.append(url_print(after_PATH))
    except NoSuchElementException:
        print(' NoSuchElementException 패 스')

    # 사진 저장
    for idx,url in enumerate(img_url):
        urlretrieve(url, f'./downloads/maxwell/'+str(cnt)+'-'+ str(idx+1) +'.jpg')
    cnt += 1

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

