#-*- coding = utf-8 -*-
#@Time : 2022/07/14 10:00
#@Author : qu6zhi
#@File : Z.py
#@Software : VScode


from cgitb import html
from distutils.filelist import findall
from sre_constants import CATEGORY_UNI_NOT_LINEBREAK
#import imp
from types import AsyncGeneratorType
from urllib import response
from bs4 import BeautifulSoup                               # 网页解析，获取数据
import re                                                   # 正则表达式，进行文字匹配
import urllib.request,urllib.error
from requests import head                                   # 指定 URL，获取网页数据
import xlwt                                                 # 进行 excel操作
import sqlite3                                              # 进行 SQLite 数据库操作
import ssl                                                  # 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

def main():

    baseurl = "https://movie.douban.com/top250?start="

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"

    # 3.保存数据
    #saveData(savepath)

    # askURL("https://movie.douban.com/top250?start=")

# 全局变量
# 影片详情链接规则
findLink = re.compile(r'<a href="(.*?)">')                  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)          # re.S 让换行符包含在字符中，忽略换行符
# 影片名称
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)<span>')
# 影评人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd =re.compile(r'<p class="">(.*)</p>',re.S)            # re.S，忽略换行符


# 爬取网页（函数）
def getData(baseurl):
    datalist = []
    for i in range(0,10):                                   # 调用获取页面信息的函数，10次，每次25条
        url = baseurl + str(i*25)                           
        html = askURL(url)                                  # 保存获取到的网页源码

    # 2.逐一解析数据
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="item"):
                                                            #查找符合要求的字符串，生成列表
        #print(item)                                        # 测试：查看电影item全部信息
        data = []                                           # 保存一步电影的所有信息
        item = str(item)         


        # 影片详情链接
        link = re.findall(findLink,item) [0]                # re 库，用来通过正则表达式查找指定的字符串
        data.append(link)                                   # 添加链接
        imgSrc = re.findall(findImgSrc,item)[0]             
        data.append(imgSrc)                                 # 添加图片
        titles = re.findall(findTitle,item)                 # 片名，可能只有中文名，没有外文名
        if (len(titles) == 2):
            otitle = titles[0]                              # 添加中文名
            data.append(otitle)
            otitle = titles[1].replace("/","")              # 去掉无关的符号
            data.append(otitle)                             # 添加外国名
        else:
            data.append(titles[0])
            data.append(' ')                                 # 外国名留空

        # print('title result: ', titles)
        # print('rating result: ', re.findall(findRating,item))
        # rating = re.findall(findRating,item)[0]
        # data.append(rating)                                 # 添加评分

        judgeNum = re.findall(findJudge,item)[0]
        data.append(judgeNum)                               # 添加评价人数

        inq = re.findall(findInq,item)
        if len(inq) != 0:
            inq = inq[0].replace("。","")                   # 去掉句号
            data.append(inq)                                # 添加概述
        else:
            data.append(" ")                                # 留空

        bd = re.findall(findBd,item)[0]
        bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)              # 去掉<br>
        bd = re.sub('/'," ",bd)                             # 替换 /
        data.append(bd.strip())                             # 去掉前后的空格

        datalist.append(data)                               #  把处理好的一部电影信息放入datalist

    print(datalist)                                         # 测试
    return datalist

# 得到指定一个URL的网页内容
# head，模拟浏览器头部信息，向豆瓣服务器发送消息
# 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的信息
def askURL(url):
    # 伪装的浏览器
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print("[success-html]: ",html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print("[error-code]: ",e.code)
        if hasattr(e,"reason"):
            print("[error-reason]: ",e.reason)
    return html

# 保存数据（函数）
def saveData(savepath):
    print("save......")

if __name__ == "__main__":           # 当程序执行时
# 调用函数
    main()
