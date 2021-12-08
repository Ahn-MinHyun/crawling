from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve, Request, urlopen   
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys


# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# print(PROJECT_ROOT)
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")


# # browser = webdriver.Chrome('/Users/mac/Desktop/bbz/crawling/crawling/chromedriver') #usr/bin

# # cnt = 1
# # folder = './downloads/wellkin/'
# # img_url =[]
# # for page in range(1, 22+1):
# #     print('page : '+ str(page))
# #     url = "https://www.wellkin.co.kr/m/html/success_01.asp?nPage="+str(page)

# #     browser.get(url)
# #     browser.implicitly_wait(time_to_wait=10)

# #     def url_print(PATH):
# #         img = browser.find_element_by_xpath(PATH).get_attribute('src')
# #         # before_url = img.value_of_css_property('background-image')
# #         # before_url = before_url.lstrip('url("').rstrip('")')
# #         return img

# #     def text_print(PATH):
# #         info_text = browser.find_element_by_xpath(PATH)
# #         return info_text.text

 

# #     for i in range(3,5+2+1):
# #         # img_url =[] 
# #         info_text= []
# #         print(i)
# #         if page == 22:
# #         #img_url
# #             if i == 3:
# #                 info_PATH = '//*[@id="container"]/div[3]/a[2]'
# #             if i == 7:
# #                 pass
# #             else:
# #                 info_PATH = '//*[@id="container"]/div['+str(i)+']/a' #4
# #         else :
# #             if i == 3:
# #                 info_PATH = '//*[@id="container"]/div[3]/a[2]'
# #             else:
# #                 info_PATH = '//*[@id="container"]/div['+str(i)+']/a' #4
# #             # //*[@id="container"]/div['+str(i+2)+']/a
# #             # //*[@id="container"]/div[4]/a
# #             # //*[@id="container"]/div[5]/a
# #             # //*[@id="container"]/div[6]/a
# #             # //*[@id="container"]/div[7]/a
# #         info_browser = browser.find_element_by_xpath(info_PATH)
# #         info_browser.send_keys(Keys.ENTER)
# #         browser.implicitly_wait(time_to_wait=10)

# #         try :
# #         # 예외 처리필요 
# #             before_PATH = '//*[@id="body_wrap"]/div[2]/div[1]/div[1]/img'
# #             img_url.append(url_print(before_PATH))
# #             after_PATH='//*[@id="body_wrap"]/div[2]/div[1]/div[2]/img'
# #             img_url.append(url_print(after_PATH))

# #         except NoSuchElementException:
# #             print(' NoSuchElementException 패 스')

# #         #환자정보 txt
# #         # classi_PATH  = '//*[@id="body_wrap"]/div[1]/ul/li[2]/span'
# #         # info_text.append(text_print(classi_PATH))
        
# #         # try :
# #         #     # 초기상태 
# #         #     info_text_1 = '//*[@id="tab-1"]'
# #         #     info_text.append(text_print(info_text_1))

# #         #     # 초기 진단
# #         #     info_text_2 = '//*[@id="tab-2"]'
# #         #     info_text.append(text_print(info_text_2))

# #         # except NoSuchElementException:
# #         #     print(' NoSuchElementException 패 스')
# #         # # txt저장
# #         # f = open(folder+str(cnt)+".txt", 'w')
# #         # f.write('\n\n'.join(info_text))
# #         # f.close()
        
# #         # # 사진 저장
# #         # for idx,url in enumerate(img_url):
# #         #     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
# #         #     urlretrieve(url, f'./downloads/wellkin/'+str(cnt)+'-'+ str(idx+1) +'.jpg')
# #         cnt += 1
# #         # print(img_url)
# #         browser.back()
# # print(img_url)
    # browser.close()
img_urls = ['https://www.wellkin.co.kr/upfiles/sdiary/bhhtm_01.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/bhhtm_02.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/hltm_01.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/hltm_02.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC12_132.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC13_132.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC10_132.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC11_132.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC2_132.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC3_132.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC8_132.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC9_132.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC6_132.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC7_132.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%97%A03_1.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%97%A04_1.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%97%A01.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%97%A02.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%9B%90%ED%98%955.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%9B%90%ED%98%956.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%9B%90%ED%98%953.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%9B%90%ED%98%954.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/1_6.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/2_1.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%989.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%9810.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%987.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%988.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%985.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%986.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%983.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%984.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%98.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EC%BA%A1%EC%B2%982.JPG', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC46.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC47.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC44.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC45.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC42.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC43.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC40.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC41.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC38.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC39.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC36.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC37.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC34.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC35.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC32.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC33.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC30.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC31.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC28.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC29.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC26.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC27.png', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC24.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC25.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC22.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC23.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC20.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC21.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC18.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC19.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC16.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC17.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC14.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC15.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC4.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/%EA%B7%B8%EB%A6%BC5.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/01_7.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/02_9.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/01_6.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/02_5.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/01_5.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/02_3.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/01_4.jpg', 'https://www.wellkin.co.kr/upfiles/sdiary/02.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk0028-1.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk0028-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00420.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00420-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00226.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00226-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00146.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00146-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00592.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00592-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk002117.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk002117-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk001467.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk001467-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00390.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00390-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00282.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00282-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk0037.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk0037-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk0065-1.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk0065-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00595-1.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00595-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00148.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00148-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00124.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00124-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00149-1.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00149-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00685.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00685-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00637.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00637-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00248.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00248-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00449.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00449-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00775.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00775-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk005711.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk005711-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk001239.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk001239-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00734.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00734-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00823.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00823-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00163.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00163-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00288.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00288-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00185.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00185-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00796.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00796-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00178.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00178-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00115.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00115-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00188.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00188-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00194.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00194-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00105.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00105-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00472.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00472-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00241.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00241-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00499.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00499-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00571.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00571-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00921.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00921-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00516.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/wk00516-2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/I10631-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/I10631-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10215-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10215-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10221-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10221-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10401-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10401-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/C10801-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/C10801-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/R10093-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/R10093-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/I10632-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/I10632-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/C10802-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/C10802-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10220-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10220-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10219-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10219-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10218-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10218-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10212-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10212-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10301-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/T10301-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10409-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10409-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10406-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10406-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10403-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10403-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10402-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/Y10402-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10223-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10223-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10222-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10222-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10219-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10219-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10217-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10217-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10209-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/KN10209-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/M10010-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/M10010-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/M10009-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/M10009-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/100028-18-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/100028-18-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/100028-1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/100028-2_1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/K10401-1_1.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/K10401-2.bmp', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%EC%B5%9C%EC%8A%B9%ED%83%9C1.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%EC%B5%9C%EC%8A%B9%ED%83%9C2.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%ED%99%A9%EB%B3%91%EC%B2%A01.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%ED%99%A9%EB%B3%91%EC%B2%A02.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%EA%B9%80%EC%A0%95%EC%9A%B01.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%EA%B9%80%EC%A0%95%EC%9A%B02.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%EA%B9%80%EC%A0%95%EC%9A%B01.jpg', 'https://www.wellkin.co.kr/2007/upload_files/sdiary/small/%EA%B9%80%EC%A0%95%EC%9A%B02.jpg']
# print(len(img_urls))

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
# img_folder = './downloads/wellkin/'
# cnt = 1
# if not os.path.isdir(img_folder) :
#     os.mkdir(img_folder)
# for img_url in img_urls:
#     req = Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}) 
#     urlretrieve(img_url, f'./downloads/wellkin/'+str(cnt)+'.jpg')
#     # f.close()
#     cnt +=1

#         browser.back()

#     browser.close()
img_folder = './downloads/wellkin/'
img_url = 'http://www.drscalp.com/data/file/case/thumb-1994075273_FTp2eKd5_f2ed03e1e347e8d54d5914958505d86a04d612ae_174x124.jpg'
# 
req = Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'})
if not os.path.isdir(img_folder) :
    os.mkdir(img_folder) 
urlretrieve(img_url, f'./downloads/wellkin/'+str(1)+'.jpg')
