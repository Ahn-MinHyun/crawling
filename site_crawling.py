from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from openpyxl.styles import PatternFill, Color
from openpyxl import Workbook
import os
# 텍스트 가져오는 함수
def text_print(browser,PATH):
    info_text = browser.find_element_by_xpath(PATH)
    return info_text.text

# 이미지 주소 가져오는 함수
def url_print(browser,PATH):
    # img = browser.find_element_by_xpath(PATH)
    # before_url = img.value_of_css_property('background-image')
    # before_url = before_url.lstrip('url("').rstrip('")')
    # return before_url
    img = browser.find_element_by_xpath(PATH).get_attribute("src")
    return img

# 엑셀 파일 
wb = Workbook()
sheet = wb.active
col = ['요리명', '서브타이틀','요리 설명', '요리이미지주소', '인분','재료1','재료2','재료3','재료4',
       '카테고리1', '조리법1', '조리법이미지1', '조리법2','조리법이미지2', 
       '조리법3', '조리법이미지3', '조리법4','조리법이미지4', 
       '조리법5', '조리법이미지5','조리법6', '조리법이미지6','조리법7', '조리법이미지7',
       '조리법8', '조리법이미지8','조리법9', '조리법이미지9','조리법10', '조리법이미지10']
sheet.append(col)
wb.save("./refri2.xlsx")

# chromedriver
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
print(PROJECT_ROOT)
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
browser = webdriver.Chrome('/Users/mac/Desktop/bbz/crawling/crawling/chromedriver') # 크롬드라이버 주소

for Theme in range(3,25+1): #1,25+1
    page = 1 # 1
    while 1:
            url = 'https://2bob.co.kr/recipe.php?id=list&fKeyList=&fKeyValue=&eTheme='+str(Theme)+'&OrderCondition=&OrderBy=&page='+str(page)
            browser.get(url)
            browser.implicitly_wait(time_to_wait=10)

            #  카테고리 명 
            category = text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[1]/h2')

            try :
                for content in range(1,20+1):
                    
                    # 음식레시피 열기
                    info_PATH = '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/ul/li['+str(content)+']/a'
                    info_browser = browser.find_element_by_xpath(info_PATH)
                    info_browser.click()
                    browser.implicitly_wait(time_to_wait=5)

                    
                    # 레시피를 저장할 딕셔너리
                    recipedata_dict = dict.fromkeys(col)
                    recipedata_dict['요리명']= text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]/div[2]/h2')
                    recipedata_dict['서브타이틀'] =text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]/div[2]/p')
                    recipedata_dict['요리 설명'] = text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]/div[2]/div') 
                    recipedata_dict['요리이미지주소'] = url_print(browser, '//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[1]/img')
                    recipedata_dict['카테고리1'] = category
                    recipedata_dict['인분'] = text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]/div[3]/div[1]/span')
                    # 필수재료 양념, 육수재료, 선택재료
                    try :
                        for number in range(1,4+1):
                            recipedata_dict['재료'+str(number)] = text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[2]/div[2]/div[3]/div['+str(number+1)+']')
                    except NoSuchElementException :
                        print('pass')
                        pass
                    finally: 
                        
                        #조리법
                        try : 
                            for number in range(1, 10+1):
                                recipedata_dict['조리법'+str(number)] = text_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[3]/ul/li[1]/div['+str(number)+']/div[2]/div[2]/div')
                                recipedata_dict['조리법이미지'+str(number)] = url_print(browser,'//*[@id="con_wrapper"]/div[5]/div[2]/div[3]/ul/li[1]/div['+str(number)+']/div[1]/img')
                            
                        except NoSuchElementException:
                            print('pass')
                            pass
                        finally:
                            print(recipedata_dict.values())
                            sheet.append(list(recipedata_dict.values()))
                            wb.save("./refri2.xlsx")
                            browser.back()
                page += 1 
                print(page)

            except NoSuchElementException:
                print('break')
                break
             

wb.close()


#             wb.save("./refri.xlsx")

#             page += 1
        # try :
        # 

    
    








# info_PATH = '//*[@id="recipe_list"]/li[1]/a'
# info_browser = browser.find_element_by_xpath(info_PATH)

# info_browser.click()

# # 이미지 주소 가져오는 함수
# def url_print(browser,PATH):
#     img = browser.find_element_by_xpath(PATH)
#     before_url = img.value_of_css_property('background-image')
#     before_url = before_url.lstrip('url("').rstrip('")')
#     return before_url
#     # before_url = img.value_of_css_property('background-image')
#     # before_url = before_url.lstrip('url("').rstrip('")')
#     # return img 
# # 텍스트 가져오는 함수
# def text_print(browser,PATH):
#     info_text = browser.find_element_by_xpath(PATH)
#     return info_text.text

# cnt = 1
# for img_number in range(1,12+1): # 페이지의 이미지 장수
#     # 이미지 주소리스트 
#     img_url =[] 
#     # 텍스트 리스트 
#     info_text= [] 

#     try :
#         before_PATH = '//*[@id="container-async"]/div/div[1]/div['+str(img_number)+']/div[1]/div[1]'
#                         # //*[@id="pageJissekiMan"]/div[2]/div[1]/ul/li[2]/div/a[1]/img
#         img_url.append(url_print(before_PATH))
#         after_PATH= '//*[@id="container-async"]/div/div[1]/div['+str(img_number)+']/div[1]/div[3]'
#         img_url.append(url_print(after_PATH))
#     except NoSuchElementException:
#         print(' NoSuchElementException 패 스')

#     # 사진 저장
#     for idx,url in enumerate(img_url):
#         urlretrieve(url, f'./downloads/maxwell/'+str(cnt)+'-'+ str(idx+1) +'.jpg')
#     cnt += 1

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

