import requests

url = "http://122.207.209.2/api.php/check"

payload={}
headers = {
  'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7',
  'Connection':'keep-alive',
  'Cookie': 'PHPSESSID=c3ep7l74n7sapu1bfenvpdujl3; uservisit=1; redirect_url=%2Fhome%2Fweb%2Fseat%2Farea%2F1; PHPSESSID=gvu5sm88eoiu6bovvic8pp5ej0',
  'Host': '122.207.209.2',
  'Referer':'http://122.207.209.2/home/web/seat/area/1',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
