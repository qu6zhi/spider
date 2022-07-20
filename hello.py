#-*- coding = utf-8 -*-
#@Time : 2022/07/14 10:00
#@Author : qu6zhi
#@File : Z.py
#@Software : VScode


from cgitb import html
#import imp
from types import AsyncGeneratorType
from urllib import response
from bs4 import BeautifulSoup       # 网页解析，获取数据
import re                           # 正则表达式，进行文字匹配
import urllib.request,urllib.error
from requests import head           # 指定 URL，获取网页数据
import xlwt                         # 进行 excel操作
import sqlite3                      # 进行 SQLite 数据库操作
import ssl                          # 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

def main():

    baseurl = "https://movie.douban.com/top250?start="

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"

    # 3.保存数据
    #saveData(savepath)

    # askURL("https://movie.douban.com/top250?start=")

# 影片详情链接规则
findLink = re.compile(r'<a href="(.*?)">')             # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)       # re.S 让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)<span>')
# 影评人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd =re.compile(r'<p class="">(.*)</p>',re.S)


# 爬取网页（函数）
def getData(baseurl):
    datalist = []
    for i in range(0,10):                   # 调用获取页面信息的函数，10次，每次25条
        url = baseurl + str(i*25)
        html = askURL(url)                 # 保存获取到的网页源码

    # 2.逐一解析数据
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="item"):
                                            #查找符合要求的字符串，生成列表
        #print()                            # 测试：查看电影item全部信息
        data = []                           # 保存一步电影的所有信息
        item = str(item)         


        # 影片详情链接
        link = re.findall(findLink,item) [0]               # re 库，用来通过正则表达式查找指定的字符串
        data.append(link)                                   # 添加链接
        imgSrc = re.findall(findImgSrc,item)[0]             
        data.append(imgSrc)                                 # 添加图片
        

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
        print("[success-html]: ",html)
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
