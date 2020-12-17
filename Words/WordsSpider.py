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
        html = response.read().decode("utf-8")
        #返回html页面数据，utf-8方式乱码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, "code")

        if hasattr(e, "reason"):
            print(e.reason)
    return html
def getData(id):
    page = askURL("http://www.jiyidanci.com/enz.asp?y="+"2")
    f = open("index.html", "w+", encoding="utf-8")
    f.write(page)
    f.close()
def readData(page,id):
    # f = open("index.html", "r", encoding="utf-8")
    resultList=[]
    resultList.append(id)
    soup = bs4.BeautifulSoup(page, 'html.parser')
    resultList.append(soup.find("div",class_="bt").text) # 中文意思
    results = soup.find_all("div",class_="nr",limit=4)
    for res in results: #遍历每一个结果
        if "2020" in res.text:
            resultList.append("") #替换为空，而不是时间
        else:
            resultList.append(res.text.replace("\n", "").replace("\"", ""))  # 去除所有的双引号，所有的空格，所有的换行符)
    # print(resultList)
    # if(len(resultList))
    return resultList
#     使用text属性直接可以获取每个元素的值

def loopGetData(startId,endId):
    result = []
    # x是当前处理的id
    for x in range(startId,endId):
        # print("we are processing"+x.__str__())
        page = askURL("http://www.jiyidanci.com/enz.asp?y=" + x.__str__())
        result.append(readData(page,x))
        if(x%5==0):
            print("saving to csv"+"  current id is"+x.__str__())
            saveFile(result)
            result.clear()
    saveFile(result)

def saveFile(data):
    file = open('./data.csv', 'a+', newline='',encoding="utf-8")
    with file:
        write = csv.writer(file)
        write.writerows(data)
        #使用csv库把文件写进去

def main():
    stardId=796
    endId=1000
    loopGetData(stardId,endId)

if __name__ == "__main__":
    main()
