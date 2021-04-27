import requests
r=requests.get('http://www.cmpbook.com/stackroom.php?id=23503')
r.encoding='GBK'
print(r.text)  #"Company":"广州新璟汽车有限公司"