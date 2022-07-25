#-*- coding = utf-8 -*-
#@Time : 2022/07/22 16:00
#@Author : qu6zhi
#@File : MYxlwt.py
#@Software : VScode

import xlwt


# # 创建workbook对象，可以理解为一个excel文件
# oneWorkBook = xlwt.Workbook(encoding = "utf-8")

# # 创建工作表，可以理解为一个excel文件中的一个sheet
# oneWorkSheet = oneWorkBook.add_sheet('sheet1')

# # 写入数据，第一个参数“行”，第二个参数“列”，第三个参数“内容”
# oneWorkSheet.write(0,0,'hello')

# # 生成excel文件，保存数据表
# oneWorkBook.save('XLWTstudent.xls')                         


# 9981
workbook = xlwt.Workbook(encoding="utf-8")                        # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')                          # 创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d "%(j+1,i+1,(j+1)*(i+1)))

workbook.save('XLWT9981.xls')                                     # 保存数据表
