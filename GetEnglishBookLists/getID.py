import urllib

import requests
import re

def getID():
  url = "http://cmpbook.com/search.php?action=advanced"

  headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://cmpbook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://cmpbook.com/stackroom.php?id=46698',
    'Accept-Language': 'en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'BOKADOTCNSITEENGINE=99waGt; maintab=news'
  }

  file = open("book_isbn")
  data = file.readlines()
  id_list = []
  for i in data:
    payload = 'searchword=' + i.__str__() + '&flag=isbn&searchtype=stackroom&submit.x=32&submit.y=17'
    payload = payload.replace("\n", "")
    response = requests.request("POST", url, headers=headers, data=payload)
    str = response.text
    reslut_id = re.findall("id=(.*?)'<", str)
    if (len(reslut_id) != 1):
      id_list.append('null')
    else:
      id_list.append(reslut_id[0])

    print(id_list)
  file.close()

def getBrief():
  file = open("book_ID.txt",'r')
  data = file.readlines()
  id_list = []
  for i in data:
    # payload = 'searchword=' + i.__str__() + '&flag=isbn&searchtype=stackroom&submit.x=32&submit.y=17'
    i = i.replace("\n", "")
    print(i)
  url = "http://www.cmpbook.com/stackroom.php?id="+i

  payload = {}
  headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'BOKADOTCNSITEENGINE=EDRCGS; BOKADOTCNSITEENGINE=ywTlTu'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)
  exit()

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
    response.encoding='gbk'
  return response.text


html = askURL("http://www.cmpbook.com/stackroom.php?id=23503")
print(html)

