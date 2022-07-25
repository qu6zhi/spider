#-*- coding = utf-8 -*-
#@Time : 2022/07/22 16:00
#@Author : qu6zhi
#@File : openpyxl.py
#@Software : VScode

from dataclasses import field
import openpyxl
from openpyxl import Workbook

# # 创建workbook对象，可以理解为一个excel文件
# workBook1 = xlwt.workBook(encoding = "utf-8")

# # 创建工作表，可以理解为一个excel文件中的一个sheet
# oneWorkSheet = workBook1.add_sheet('sheet1')

# # 写入数据，第一个参数“行”，第二个参数“列”，第三个参数“内容”
# oneWorkSheet.write(0,0,'hello')

# # 生成excel文件，保存数据表
# workBook1.save('student.xls')                         

#
#
#
# 创建workbook对象，可以理解为一个excel文件
workbook = Workbook()

# 激活表格，获取被激活的 worksheet
worksheet = workbook.active

# 定义内容
fields = ['name', 'age', 'sex']

# 填入首行内容
worksheet.append(fields)

# 写入数据，第一个参数“行”，第二个参数“列”，第三个参数“内容”
worksheet.append(['Jacky', '23', 'male'])

# 保存数据表
workbook.save('test.xlsx')
