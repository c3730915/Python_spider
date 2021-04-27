from lxml import etree
# print(html_data)
import requests
import codecs
def saveUrlAsUtf(base):
    response = requests.get(
        'http://cmpbook.com/searchbook.php?pagestart='+str(base)+"&action=search&title=&series=%BE%AD%B5%E4%D4%AD%B0%E6&isbn=&publictime=&storetime=&searchword=&s1=&s2=&Submit=%CB%D1%CB%F7&orderby=publictime")
    html = str(response.content.decode('gb2312').encode('utf-8'), 'utf-8')
    file = codecs.open("SearchReslutPages/"+base.__str__()+".html", "w", "utf-8")
    file.write(html)
    file.close()
# saveUrlAsUtf()
def xpath():
    # html = etree.parse('text.html', etree.HTMLParser())
    # result = etree.tostring(html)
    # html_data = html.xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr')
    hxml = etree.HTML(open('text.html', 'r').read())
    htree = etree.ElementTree(hxml)

    html_data = htree.xpath("/html/body/table/tbody/tr/td")

    data_list = html_data[8].xpath("//span/text()")
    for d in data_list:
        print(d)

def savePages():
    for i in range(1, 85):
        # baseUrl = 'http://cmpbook.com/searchbook.php?pagestart=' + i.__str__() + '&action=search&title=&series=%BE%AD%B5%E4%D4%AD%B0%E6&isbn=&publictime=&storetime=&searchword=&s1=&s2=&Submit=%CB%D1%CB%F7&orderby=publictime'
        saveUrlAsUtf(i)
        print("Processing"+i.__str__)
        # resp = requests.get(baseUrl)
        # html = str(resp.content.decode('gb2312').encode('utf-8'), 'utf-8')


savePages()
# print(html)

# f.write(html)
