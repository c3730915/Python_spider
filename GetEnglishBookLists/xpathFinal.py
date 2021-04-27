import codecs
import csv

from lxml import etree
import requests
def readFile(base):
    # 这个地方可能出错，根据网页编码不同，有 utf-8 和gbk
    file = codecs.open("SearchReslutPages/"+str(base)+".html", "r", "gbk")

    html = file.read()
    return html

def getData(basePage):
    # 调用此函数，传入basePage 即第几页 然后返回数据列表

    html_data = readFile(basePage)
    # print(html_data)
    hxml = etree.HTML(html_data)
    htree = etree.ElementTree(hxml)
    # data_list = htree.xpath("//a[starts-with(@href, '/stackroom.php?')]/text()")
    # data_list = htree.xpath("//span/text()")
    # 拿到标题
    data_title = htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//span[@class='font09']/text()")

    # 拿到价格
    data_price_tmp = htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//span[@class='font04']/text()")
    data_price=[]
    for item in data_price_tmp:
        data_price.append(item[1:])

    # 同时拿到isbn和系列
    data_isbn_series =  htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//td[@width='50%']/span[@class='font01']/text()")
    data_isbn = []
    for i in range(0,5):
        str = data_isbn_series[2*(i)]
        str = str[9:]
        data_isbn.append(str)
    #拿到isbn

    # 拿到作者以及一大堆信息，六个为一组
    # 分别为 作者，ISBN 丛书名 日期 版次 价格（null)
    data_list2 = htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//td[@align='left']/span[@class='font01']/text()")

    # 拿到作者
    data_author = []
    data_date = []

    # 拿到图书日期

    for i in range(0,5):
        str_author = data_list2[i*6]
        # 处理作者的空格字符
        str_author=str_author.strip().replace(u'\u3000', u' ').replace(u'\xa0', u' ').replace(" ","")
        data_author.append(str_author)
        data_date.append(data_list2[i*6+3][3:])
    # 拿到了图片link！
    data_pics_tmp = htree.xpath("//img[@width='76']/@src")
    data_id= htree.xpath("//tr/td/table[starts-with(@width,'95%') and @class='table01']//td[class='font09']/a")
    print(data_id)
    exit()
    data_pics = []
    pic_base_url = "http://cmpbook.com/"
    for item in data_pics_tmp:
        data_pics.append(pic_base_url+item)

    # 除了内容摘要以外，所有的数据均已完成提取，数据为 data_title, data_author, data_isbn, data_date, data_price, data_pics
    data_result = []
    # 用于临时存储每本书的信息
    for i in range(0,5):
        book_info_tmp = []
        book_info_tmp.append(data_title[i])
        book_info_tmp.append(data_author[i])
        book_info_tmp.append(data_isbn[i])
        book_info_tmp.append(data_date[i])
        book_info_tmp.append(data_price[i])
        book_info_tmp.append(data_pics[i])
        data_result.append(book_info_tmp)

    return data_result


def saveCsv(data):
    fields = ['title','author','isbn','date','price','pics']
    with open('dataList.csv', 'a',encoding='utf-8') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data)



total_result = []
for i in range(1,28):
    data = getData(i)
    for item in data:
        total_result.append(item)
    print("Processing" + i.__str__())
print("Writing to csv")
saveCsv(total_result)
