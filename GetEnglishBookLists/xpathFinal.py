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
    # data_list = htree.xpath("//a[starts-with(@href, '/stackroom.php?')]/text()")
    # data_list = htree.xpath("//span/text()")
    # 拿到标题
    data_title = htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//span[@class='font09']/text()")

    # 拿到价格
    data_price = htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//span[@class='font04']/text()")

    # 同时拿到isbn和系列
    data_isbn_series =  htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//td[@width='50%']/span[@class='font01']/text()")

    # 拿到作者以及一大堆信息，六个为一组
    # 分别为 作者，ISBN 丛书名 日期 版次 价格（null)
    data_list2 = htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//td[@align='left']/span[@class='font01']/text()")

    # 拿到了图片link！
    data_pics = htree.xpath("//img[@width='76']/@src")
    # print(data_list2[0],data_list2[6],data_list2[12],data_list2[18],data_list2[24])
    # exit()
    for d in data_list2:
        # print(type(d))
        # etree.tostring(d)

        print(d)
        print("=====================================")

getData()

exit()