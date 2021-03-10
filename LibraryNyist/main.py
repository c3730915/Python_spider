import re

import chaojiying
import requests


def getCode():
    # 直接返回一个验证码，方便登录！
    url = "http://122.207.209.2/api.php/check"
    payload = {}
    headers = {
        'Referer': 'http://122.207.209.2/home/web/seat/area/1',
        'Cookie': 'PHPSESSID=eecgaq2licine3bu94b6oi1ts4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    code = verifyCode(response.content)
    return code

def login(username="1815925161",password="c6f057b86584942e415435ffb1fa93d4"):
    # 登录函数
    print("Getting verify code.....")
    verifyCode = getCode()

    url = "http://122.207.209.2/api.php/login?username="+username.__str__()+"&password="+password.__str__()+"&verify="+verifyCode
    # print(url)
    # return

    payload = {}
    headers = {
        'Referer': 'http://122.207.209.2/home/web/seat/area/1',
        'Cookie': 'PHPSESSID=eecgaq2licine3bu94b6oi1ts4'
    }
    print("Trying to log in....")

    response = requests.request("GET", url, headers=headers, data=payload)
    return re.findall(r'access_token":"(.*?)"', response.text)[0]

def verifyCode(img):
    client = chaojiying.Chaojiying_Client('c3730915', '9DpxzsJbNBJLB.F', '913619')
    data = client.PostPic(img,"4004")
    print(data)
    return (data['pic_str'])

def getFreeRoom(area="8",year="2021",month="03",day="11",flag =0):
    if(flag==0):
        #上午进行预定
        startTime = "08"
        endTime = "12"
    else:
        startTime = "14"
        endTime = "22"

    # 2021 - 3 - 11 & startTime = 14:30 & endTime = 21:30
    # 参数说明：area 预定区域，剩下三个为年月日
    # flag代表是上午还是晚上，上午为0，下午为1
    #开始时间还可以为14:30 结束时间为21:30
    url = "http://122.207.209.2/api.php/spaces_old?area="+area+"&segment=1303812&day="+year+"-"+month+"-"+day+"&startTime="+startTime+"%3A00&endTime="+endTime+"%3A00"
    headers = {
        'Referer': 'http://112.207.209.2/web/seat3?area=6&segment=1302598&day=2021-3-11&startTime=07:50&endTime=12:00',
        'Cookie': 'PHPSESSID=j007enuovkd4c0r0l7o579g5a7'}

    response = requests.request("GET", url, headers=headers)
    print(type(response))

    return response.json()['data']['list']

def getSeat(seatList):
    for seat in seatList:
        if (seat['status'] == 1):
            return seat['id']
accessToken = login()
print(accessToken+"登陆成功！")

freeSeats = getFreeRoom()
print("已经发现空位，空位id是：")
print(getSeat(freeSeats))

# print(type(getFreeRoom()))


result = login()
if(result.__len__()<=10):
    print("Log in error! Please try again!")
else:
    print("Log in successfully! Token is" +result )



