
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
findLink = re.compile(r'<a href="(.*?)">') #create re expression, referring a rule
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) # S to ignore line break
findTitle = re.compile(r'<span class="title"(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)   #ignore linebreak

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl+str(i*25)
        html = askURL(url)
        #print("this is",str(i),"th page")
        # print(html)
        # f = open(str("douban"+str(i)+"html"),"w")
        # f.write(str(html))
        #time.sleep(3)
        soup = bs4.BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_ = "item"):
            # print(item) #test item.
            data = [] #store the whole info of a movie
            item = str(item)
            # print(item)
            # f = open("temp.html","w")
            # f.write(item)
            link = re.findall(findLink,item)[0] #re library used to search by using re expression
            imgSrc = re.findall(findImgSrc,item)[0]
            title = re.findall(findTitle,item) #other languages in tiles
            rating = re.findall(findRating,item)[0]
            judgeNum=re.findall(findJudge,item)[0]
            inq = re.findall(findInq,item) #Introduction of movies
            # bd = re.findall(findBd,item)[0]
            #
            # bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            # bd = re.sub("/"," ",bd)
            # data.append(bd.strip()) #remove space


            if len(inq) ==0:
                data.append(" ")

            if(len(title) == 2):
                ctitle = str(title[0]).replace('>',"",1)
                data.append(ctitle)
                otitle = title[1].replace("/","") #remove /, add forigen languages
            else:
                data.append(title[0])
                data.append(" ") #empty item for excel

            data.append(link)
            data.append(imgSrc)
            data.append(str(title).replace('>','',1))
            data.append(rating)
            data.append(judgeNum)
            print(data)
            datalist.append(data)
           # print(datalist)

            # print(link)

    return datalist

def saveData(savepath=".\\"):
    print()

def getData2(baseurl):
    datalist = []
    for i in range(0, 2):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)   #测试：查看电影item全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)

            # 影片详情的链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)  # 添加链接

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片

            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名，没有外国名
            if (len(titles) == 2):
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0].replace('\\xa0/\\xa0',''))
                data.append(' ')  # 外国名字留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 提加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影信息放入datalist
            print(data)

    return datalist


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
