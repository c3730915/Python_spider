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

def getData():
    f = open("index.html", "r", encoding="utf-8")
    html = f.read()
    f.close()
    #为了方便调试，将之前爬取的页面存到本地
    # pattern = re.compile(r'<td data-v-2a8fd7e4=*>*<!')
    soup = bs4.BeautifulSoup(html)
    result = soup.find_all("tr")
    #用bs4的库，把素有tr标签解析出来，因为不是标准的html（由前端编译而成）无法用固定的库进行分析
    Total = list()
    for res in result:
        res = str(res).replace("\n", "").replace(" ", "").replace("\"", "")  # 去除所有的双引号，所有的空格，所有的换行符
        # score = str(re.findall("v-2a8fd7e4=>(\d\d\d)", str(res)))
        name = str(re.findall("/institution.*>(.*)</a", res)).replace("['", "").replace("']", "")
        #高校名称进行单独爬取
        tmp = re.findall("<tddata-v-2a8fd7e4=>(.*?)<!---->", res)
        ReslutList = list(tmp)
        ReslutList.insert(0, name)
        #把名字插入列表头
        Total.append(ReslutList)
        #追加到总列表中

    print(Total)
    del Total[0:2]
    #除去干扰数据，因为前两条数据为空，因为网站有其他干扰 故除去
    saveFile(Total)

def saveFile(data):
    file = open('data.csv', 'w+', newline='',encoding="utf-8")

    with file:
        write = csv.writer(file)
        write.writerows(data)
        #使用csv库把文件写进去
def run():
    baseurl = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = askURL(baseurl)
    getData()

def importMysql():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='jdbc',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
    # cursor.execute('CREATE TABLE universityData (Name nvarchar(50), Ranking nvarchar(50), Area nvarchar(50),TYPE nvarchar(50),Score nvarchar(50))')
    eFile=open("data.csv",encoding='utf-8')
    eReader=csv.reader(eFile)
    for row in eReader:
            # print(row[0])
        data = (row[0],row[1],row[2],row[3],row[4])
        print(data)
        cursor.execute('insert into universityData values (%s,%s,%s,%s,%s)',data)


        # print(row)
    connection.commit()
    #提交mysql事务



