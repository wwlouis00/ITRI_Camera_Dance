import os
import openpyxl
import time
from datetime import datetime


#開啟要測試的excel檔
wb = openpyxl.load_workbook("openpyxl.xlsx")
#ws是wb.active
ws = wb.active
#輸出現在時間的檔名
now_output_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+"output.xlsx"
#陣列
s = []
ws.cell(row= 1,column= 1).value = "demo"
for i in range(1,11,1):
    s.append(i) #把數字加到列
    print(s)
    time.sleep(1)
    