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
    return response.content.decode('gb2312').encode('utf-8')


def saveFile(html):
    # str =
    open('text.html', 'w').write(html)
html = askURL('http://cmpbook.com/searchbook.php?pagestart=0&action=search&title=&series=%BE%AD%B5%E4%D4%AD%B0%E6&isbn=&publictime=&storetime=&searchword=&s1=&s2=&Submit=%CB%D1%CB%F7&orderby=publictime')
saveFile(html)
exit()



str = '<a href="/stackroom.php?id=46765" target="_blank">本书主要介绍程序设计语言的基本概念，讨论语言结构的设计问题，研究C++、Java、Pytho..</a>'

print(re.findall('<a href="/stackroom.php?id=^[0-9]*$"',str))
exit()
html = open('text.html', 'r', encoding='gbk').read()
# 以GBK编码读取，防止乱码

html.replace("摘要：" "xyz123456")

exit()
# re.findall(r"")
bs = BeautifulSoup(html, "html.parser")
sub = bs.findAll('table', {"class": "table01", "width": "400", "align": "left"})

re.findall('src="data/stackroom/(.*?)"', str(html))
re_id = re.compile('id=(.*?)"')
re_title = re.compile('target="_blank"><span class="font09">(.*?)</')
re_author = re.compile('<td align="left"><span class="font01">(.*?)<')
re_ISBN = re.compile('<span class="font01">ISBN(.*?)<')
re_series = re.compile('<span class="font01">(.*?)</span>')

result_date = re.findall('align=left><span class=font01>(.*?)</span></td>', html)

# print(result_date.count())
i = 1
book_info = []
result_info = []
book_prices =[]
book_dates = []

#书的价格和日期需要单独提取
for index in range(0, 5):
    data = result_date[index * 4 + 1]
    price = result_date[index * 4 + 3]
    data = data[3:]
    price = str(price[-7:])
    price.replace("￥", "")
    if price.__sizeof__() == 88:
        price = price[-6:]
        price = price[:-1]
    else:
        price = price[:-1]
    book_prices.append(price)
    book_dates.append(data)
    i += 1
# for ends here
print(book_prices)
print(book_dates)
for item in sub:
    tmp_str = str(item)
    print(tmp_str)

    # title
    print(re.findall(re_title,tmp_str)[0])
    # book id
    print(re.findall(re_id,tmp_str)[0])
    # book author
    print(re.findall(re_author,tmp_str)[0])
    # book ISBN
    isbn_str = re.findall(re_ISBN,tmp_str).__str__()
    isbn_str = isbn_str[isbn_str.find('：')+1:-2]
    print(isbn_str)

    # book series
    print(re.findall(re_series,tmp_str)[2])
    # print(re.findall(re_series,tmp_str))
    print("=================")
# # print(sub[4])
# for th in sub:
#     print(th.findAll('table', {"width": "95%", "class": "table01"}))
# result = sub.findAll('table', {"width": "95%", "class": "table01"})
# print(result)


# for th in sub:
#     # print(th.findAll('table', {"width": "95%", "class": "table01"}))
