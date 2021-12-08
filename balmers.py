from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException



PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print(PROJECT_ROOT)
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
cnt = 1
for page in range(109,267+1): #267+1
    # page = 17
    print('page : '+ str(page))
    url = 'https://www.balmers.co.kr/photo?is_best=0&page='+str(page)
   
    browser = webdriver.Chrome('/Users/mac/Desktop/crawling/crawling/chromedriver') #usr/bin

    browser.get(url)
    browser.implicitly_wait(time_to_wait=10)
    # page = str(2)
    # page_number = '//*[@id="container-async"]/div/ul/li['+page+']/a'

    def url_print(PATH):
        img = browser.find_element_by_xpath(PATH).get_attribute("src")
        return img
        # img = browser.find_element_by_xpath(PATH)
        # before_url = img.value_of_css_property('background-image')
        # before_url = before_url.lstrip('url("').rstrip('")')
        return before_url

    def text_print(PATH):
        info_text = browser.find_element_by_xpath(PATH)
        return info_text.text

 

    for i in range(1,12+1): # 12+1
        img_url =[] # 0.환자 1.초기상태, 2.초기검사
        info_text= [] # 홀수 초기, 짝수 호전
        print(i)
        # i = 
        # info_PATH = '//*[@id="main-wrapper"]/div[2]/div/div/div/div[1]/div['+str(i)+']/a'
        # info_browser = browser.find_element_by_xpath(info_PATH)
        # info_browser.click()
        # browser.implicitly_wait(time_to_wait=10)

        try :
        # 예외 처리필요 
            before_PATH = '//*[@id="__next"]/div/div[2]/div[4]/a['+str(i)+']/div[2]/div/div[1]/div/div[1]/img'
            img_url.append(url_print(before_PATH))
            after_PATH = '//*[@id="__next"]/div/div[2]/div[4]/a['+str(i)+']/div[2]/div/div[2]/div/div[1]/img'
            img_url.append(url_print(after_PATH))

            # before_PATH_2 = '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[2]/div[1]'
            # img_url.append(url_print(before_PATH_2))
            # after_PATH_2 = '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[2]/div[3]'
            # img_url.append(url_print(after_PATH_2))

            # before_PATH_3 = '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[3]/div[1]'
            # img_url.append(url_print(before_PATH_3))
            # after_PATH_3 = '//*[@id="main-wrapper"]/div[2]/div[2]/div[1]/div[3]/div[3]'
            # img_url.append(url_print(after_PATH_3))
        except NoSuchElementException:
            print(' NoSuchElementException 패 스')

        #환자정보
        
        try :
            # 성별
            info_text_1 = '//*[@id="__next"]/div/div[2]/div[4]/a['+str(i)+']/div[1]/div[3]/span[2]'
            info_text.append(text_print(info_text_1))

            # 탈모명
            info_text_2 = '//*[@id="__next"]/div/div[2]/div[4]/a['+str(i)+']/div[1]/div[5]/span[2]'
            info_text.append(text_print(info_text_2))

        except NoSuchElementException:
            print(' NoSuchElementException 패 스')
        # txt저장
        f = open('./downloads/balmers/'+str(cnt)+".txt", 'w')
        f.write('\n\n'.join(info_text))
        f.close()

        # # 사진 저장
        for idx,url in enumerate(img_url):
            urlretrieve(url, f'./downloads/balmers/'+str(cnt)+'-'+ str(idx+1) +'.jpg')
        cnt += 1

        # browser.back()
        print(info_text)
        print(img_url)
    
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
        # img_folder = './downloads/balmers/'
        # if not os.path.isdir(img_folder) :
        #     os.mkdir(img_folder)
#         f = open('./downloads/morak/'+str(cnt)+".txt", 'w')
#         f.write(classifi_text.text+ "\n\n"+info_text_1.text +"\n\n"+ info_text_2.text )
#         f.close()
#         cnt += 2

#         browser.back()

#     browser.close()

