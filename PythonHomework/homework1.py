import urllib

import bs4


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

def getData(html):
    soup = bs4.BeautifulSoup(html)
    result = soup.find_all("section",class_="tag issue clearfix")
    #运用bs4，通过分析网页源代码找到需要的地方是session 并且class也有相应标志
    result2=soup.find_all("div",class_="item clearfix")
    print(result2)


