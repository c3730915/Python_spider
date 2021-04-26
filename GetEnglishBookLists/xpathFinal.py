import codecs

from lxml import etree
import requests
# resp=requests.get('http://cmpbook.com/searchbook.php?pagestart=0&action=search&title=&series=%BE%AD%B5%E4%D4%AD%B0%E6&isbn=&publictime=&storetime=&searchword=&s1=&s2=&Submit=%CB%D1%CB%F7&orderby=publictime')
# open('SearchReslutPages/1.html','w').write(str(resp.content.decode('gb2312').encode('utf-8'),'utf-8'))
def readFile(base):
    file = codecs.open("SearchReslutPages/"+str(base)+".html", "r", "utf-8")
    html = file.read()
    return html

def getData():
    html_data = readFile(1)
    # print(html_data)
    hxml = etree.HTML(html_data)
    htree = etree.ElementTree(hxml)
    data_list = htree.xpath("//a[starts-with(@href, '/stackroom.php?')]/text()")
    # data_list = htree.xpath("//span/text()")
    for d in data_list:
        print(d)
        print("=====================================")

getData()

exit()