import bs4  # 网页解析，获取数据
import re  # 正则表达式
import csv
import pandas as pd
import urllib.request, urllib.error  # 制定url，获取网页
import pymysql

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"

    }
    #请求头，伪装成浏览器
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        #运用urllib库来进行请求
        html = response.read()
        #返回html页面数据，utf-8方式乱码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, "code")

        if hasattr(e, "reason"):
            print(e.reason)
    return html
def getData(page):
    soup = bs4.BeautifulSoup(page, 'html.parser')
    divs = soup.find_all("div",class_="nr",limit=20)
    for div in divs:
        print(div.find("a",href=True).attrs['href'])




getData(askURL("http://www.jiyidanci.com/index.asp?page=1"))
