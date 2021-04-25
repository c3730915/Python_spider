from bs4 import BeautifulSoup
import requests

html = "http://cmpbook.com/searchbook.php?pagestart=0&action=search&title=&series=%BE%AD%B5%E4%D4%AD%B0%E6&isbn=&publictime=&storetime=&searchword=&s1=&s2=&Submit=%CB%D1%CB%F7&orderby=publictime"
content = requests.get(html)
# print(content.content)
bs = BeautifulSoup(content, "html.parser")


