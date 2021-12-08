from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException



PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print(PROJECT_ROOT)
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

browser = webdriver.Chrome('/Users/mac/Desktop/bbz/crawling/crawling/chromedriver') #usr/bin
cnt = 1
for page in range(11, 46+1):
    # page = 17
    print('page : '+ str(page))
    url = "https://www.d-clinicgroup.jp/clinic/example/page/"+str(page)+"/"


    browser.get(url)
    browser.implicitly_wait(time_to_wait=10)
    # page = str(2)
    # page_number = '//*[@id="container-async"]/div/ul/li['+page+']/a'

    def url_print(PATH):
        img = browser.find_element_by_xpath(PATH).get_attribute("src")
        # before_url = img.value_of_css_property('background-image')
        # before_url = before_url.lstrip('url("').rstrip('")')
        return img

    def text_print(PATH):
        info_text = browser.find_element_by_xpath(PATH)
        return info_text.text

 

    for i in range(1,10+1):
        img_url =[] # 0.환자 1.초기상태, 2.초기검사
        info_text= [] # 홀수 초기, 짝수 호전
        print(i)

        try :
        # 예외 처리필요 
            before_PATH = '//*[@id="wrap_contents"]/main/section[1]/div/div/div['+str(i)+']/div[1]/div/figure[1]/img'
                         # //*[@id="wrap_contents"]/main/section[1]/div/div/div[2]/div[1]/div/figure[1]/img
            img_url.append(url_print(before_PATH))
            print(url_print(before_PATH))
            progress_PATH = '//*[@id="wrap_contents"]/main/section[1]/div/div/div['+str(i)+']/div[1]/div/figure[2]/img'
            img_url.append(url_print(progress_PATH))
            after_PATH = '//*[@id="wrap_contents"]/main/section[1]/div/div/div['+str(i)+']/div[1]/div/figure[3]/img'
            img_url.append(url_print(after_PATH))
# //*[@id="fboardlist"]/ul/li[2]/div[1]/a/img[1]
        except NoSuchElementException:
            print(' NoSuchElementException 패 스')

        # 사진 저장
        try :
            for idx,url in enumerate(img_url):
                urlretrieve(url, f'./downloads/d-clinicgroup/'+str(cnt)+'-'+ str(idx+1) +'.jpg')
        except :
            print('pass')
        cnt += 1

        # browser.back()

    # browser.close()

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

