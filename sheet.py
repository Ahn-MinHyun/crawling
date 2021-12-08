from openpyxl.styles import PatternFill, Color
from openpyxl import Workbook
import os 

# print(os.path('/Users/mac/Desktop/bbz/crawling/downloads/reve21'))

filename = '/Users/mac/Desktop/bbz/crawling/crawling/downloads/train/face'
file_list=os.listdir(filename)
print(len(file_list))

wb = Workbook()

sheet = wb.active
for file in reversed(file_list):
    if not file.endswith(".txt"):
        # print('morak/'+file)
        sheet.append(['train/face/'+file,'정면','Y','Y'])

wb.save("./result.xlsx")
