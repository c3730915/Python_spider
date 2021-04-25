import urllib

from bs4 import BeautifulSoup
import requests
import re

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
        html = response.read().decode("gbk")
        #返回html页面数据，utf-8方式乱码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, "code")

        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveFile(html):
    # str =
    open('text.html', 'w').write(html)
html = open('text.html','r').read()
# re.findall(r"")
bs = BeautifulSoup(html, "html.parser")
sub = bs.findAll('table', {"class": "table01","width": "400", "align":"left"})

re.findall('src="data/stackroom/(.*?)"',str(html))
re_id=re.compile('id=(.*?)"')
re_title=re.compile('target="_blank"><span class="font09">(.*?)</')
re_author=re.compile('<td align="left"><span class="font01">(.*?)<')
re_ISBN=re.compile('<span class="font01">ISBN(.*?)<')
re_series=re.compile('<span class="font01">(.*?)</span>')

for item in sub:
    # print(item)
    tmp_str = str (item)
    # print(re.findall(re_title,tmp_str))
    # print(re.findall(re_id,tmp_str))
    # print(re.findall(re_author,tmp_str))
    isbn_str = re.findall(re_ISBN,tmp_str).__str__()
    # isbn_str = isbn_str[isbn_str.find('：')+1:-2]
    # print(isbn_str)
    # print(re.findall(re_series,tmp_str)[2])
    print("=================")
# # print(sub[4])
# for th in sub:
#     print(th.findAll('table', {"width": "95%", "class": "table01"}))
# result = sub.findAll('table', {"width": "95%", "class": "table01"})
# print(result)


# for th in sub:
#     # print(th.findAll('table', {"width": "95%", "class": "table01"}))




