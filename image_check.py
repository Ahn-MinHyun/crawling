import cv2
# from PIL import Imageapt-get install python3-imaging
from openpyxl.styles import PatternFill, Color
from openpyxl import Workbook
import os 

# print(os.path('/Users/mac/Desktop/bbz/crawling/downloads/reve21'))

filename = '/Users/mac/Desktop/bbz/crawling/crawling/downloads/google'
file_list=os.listdir(filename)
print(len(file_list))


wb = Workbook()

sheet = wb.active
for file in reversed(file_list):
    # print(filename+'/'+file)
    if not file.endswith(".txt"):
        img = cv2.imread(filename+'/'+file)
        # print(type(img)) 
        print(filename+'/'+file)  

        try :
            h,w,c = img.shape
            if w >= 300 :
                sheet.append(['google_face/'+file,'Y', w ])
            else :
                sheet.append(['google_face/'+file,'N', w ])
        except :
            sheet.append(['google_face/'+file,'N'])
wb.save("./result.xlsx")
print('end')

# filename = '/Users/mac/Desktop/bbz/crawling/crawling/downloads/face/image00001.jpg'
# img = cv2.imread(filename)
# h,w,c = img.shape
# print(w)
# print(type(img.shape))