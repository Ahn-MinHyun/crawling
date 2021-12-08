import urllib.request
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/mac/Desktop/bbz/crawling/crawling/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("헤어라인 탈모")
# 이마라인,탈모 정면,여성탈모 이마,남성탈모 이마,넓은 이마,이마,M자탈모,헤어라인,헤어라인 탈모,남성이마 모발이식,여성이마 모발이식,남성헤어라인교정,여성헤어라인교정"
elem.send_keys(Keys.RETURN)
 
SCROLL_PAUSE_TIME = 1
 
last_height = driver.execute_script("return document.body.scrollHeight")
 
while True:
    driver.implicitly_wait(time_to_wait=10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
    time.sleep(SCROLL_PAUSE_TIME)
 
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height
 
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try :
        image.click()
        driver.implicitly_wait(time_to_wait=10)
        imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
                                             
        urllib.request.urlretrieve(imgUrl, './downloads/google/'+str(count) + ".jpg")
        print(count)
        count = count + 1
    except Exception as e:
        print(e)
    if count == 101:
        break
driver.close()