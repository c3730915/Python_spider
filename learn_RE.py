
# if __name__ == "__main__":
#     #call function
#     main(1)
# Ctrl+ ? to comment selected codes
import bs4      #网页解析，获取数据
import re       #正则表达式
import time
import urllib.request,urllib.error #制定url，获取网页
# import xlwt
# import sqlite3


def getData(baseurl):
    datalist = []
    for i in range(0,1):
        url = baseurl+str(i*25)
        html = askURL(url)
        #print("this is",str(i),"th page")
        # print(html)
        f = open(str("douban"+str(i)+"html"),"w")
        f.write(str(html))
        #time.sleep(3)
        soup = bs4.BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_ = "item"):
            #print(item) #check item info from movies
            data = [] #store the whole info of a movie
            item = str(item)
    return datalist

def saveData(savepath=".\\"):
    print()


def askURL(url):
    head = {
     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"

    }
    request = urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,"code")

        if hasattr(e,"reason"):
            print(e.reason)
    return html
# html = "https://www.douban.com"
# print(askURL(html))

baseurl = "https://movie.douban.com/top250?start="
datalist = getData(baseurl)
savepath=".\doubanmovie_TOP250.xls"
# saveData(savepath)
