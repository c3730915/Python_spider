from selenium import webdriver
# import seleniumrequests
import urllib.request
import requests
import time
import json
import chaojiying

def getCookie():
    driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    driver.get("http://122.207.209.2/home/web/seat/area/1")
    el = driver.find_element_by_class_name("login-btn").click()
    driver.find_element_by_name("username").send_keys("1815925161")
    driver.find_element_by_name("password").send_keys("000")
    img = driver.find_element_by_id("checkpic").screenshot_as_png
    cookies = driver.get_cookies()
    f = open("cookie.json", "w")
    f.write(cookies.__str__())
    f.close()
    driver.close()
    exit()
    # f = open("test.png", "wb")
    # f.write(img)
    # f.close()
    # chaojiying = chaojiying.
    # im = open('test.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    res = chaojiying.PostPic(img, 4004)
    print(res["pic_str"])
    driver.find_element_by_name('verify').send_keys(res["pic_str"])
    driver.find_element_by_class_name("ui-dialog-autofocus").click()

def getFreeRoom():
    # url = "http://122.207.209.2/api.php/space_time_buckets?day=2021-3-7&area=7"
    url = "http://122.207.209.2/api.php/spaces_old?area=7&segment=1303812&day=2021-03-07&startTime=08%3A00&endTime=12%3A00"
    headers = {'Referer':'http://112.207.209.2/web/seat3?area=6&segment=1302598&day=2021-3-7&startTime=07:50&endTime=12:00','Cookie':'PHPSESSID=j007enuovkd4c0r0l7o579g5a7'}

    response = requests.request("GET", url, headers=headers)
    print(type(response))

    return response.json()['data']['list']

def readCookie():
    with open('cookie.json') as json_file:
        data = json.load(json_file)
        # print(data[1])

readCookie()
exit()
# Chrome操作阶段
driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("http://122.207.209.2/home/web/seat/area/1")
el = driver.find_element_by_class_name("login-btn").click()
driver.find_element_by_name("username").send_keys("1815925161")
driver.find_element_by_name("password").send_keys("000")

#识别验证码
chaojiying= chaojiying.Chaojiying_Client('c3730915', '9DpxzsJbNBJLB.F', '913619')  # 用户中心>>软件ID 生成一个替换 96001
img = driver.find_element_by_id("checkpic").screenshot_as_png
res = chaojiying.PostPic(img, 4004)
driver.find_element_by_name('verify').send_keys(res["pic_str"])
driver.find_element_by_class_name("ui-dialog-autofocus").click()
time.sleep(4)
#获取cookie
cookies = driver.get_cookies()
if(cookies.__len__()==6):
    print("成功登录！")
    f = open("cookie.json", "w")
    f.write(cookies.__str__())
    f.close()
else:
    print("登陆失败！请重新登陆")

driver.close()
exit()

print(getFreeRoom())
f = open("free.json","w",encoding='UTF-8')
f.write(json.dumps(getFreeRoom()))
f.close()
# run()
