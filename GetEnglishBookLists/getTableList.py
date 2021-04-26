import urllib
from bs4 import BeautifulSoup
import requests
import re

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"

    }
    # 请求头，伪装成浏览器
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        # 运用urllib库来进行请求
        # html = response.read().decode("gbk")
        # 返回html页面数据，utf-8方式乱码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, "code")

        if hasattr(e, "reason"):
            print(e.reason)
    return response.content

# def getID(html):
books_id = []
for i in range(1,85):
    baseUrl = 'http://cmpbook.com/searchbook.php?pagestart='+i.__str__()+'&action=search&title=&series=%BE%AD%B5%E4%D4%AD%B0%E6&isbn=&publictime=&storetime=&searchword=&s1=&s2=&Submit=%CB%D1%CB%F7&orderby=publictime'
    # html = askURL(baseUrl)
    resp = requests.get(baseUrl)
    html= str(resp.content.decode('gb2312').encode('utf-8'), 'utf-8')

    bs = BeautifulSoup(html, "html.parser")
    sub = bs.findAll('table', {"class": "table01", "width": "400", "align": "left"})
    re_id = re.compile('id=(.*?)"')
    for item in sub:
        tmp_str = str(item)
        books_id.append(re.findall(re_id,tmp_str)[0])
    print("Processing" + i.__str__()+"pages")
    textfile = open("book_ID.txt", "a")
    for book_id in books_id:
        textfile.write(book_id+"\n")
    textfile.close()
    books_id.clear()


