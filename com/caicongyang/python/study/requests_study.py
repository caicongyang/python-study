#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json

# 提交表单

r = requests.get('https://www.baidu.com')

print(r.status_code)
print(r.encoding)
print(r.headers)

payload = {"key1": "value1", "key2": "value2"}
r1 = requests.put("http://httpbin.org/put", data=payload)
print(r1.text)

r2 = requests.post("http://httpbin.org/post", data=payload)
print(r2.text)


print('---------------r3----------------')

h3 = {'content-type':'text/html'}
r3 = requests.get("http://httpbin.org/html", headers=h3)
print(r3.content)
print(r3.text)




print('---------------application/json----------')
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Referer": "http://jinbao.pinduoduo.com/index?page=5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
url = "http://jinbao.pinduoduo.com/network/api/common/goodsList"
pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}
response = requests.post(url, data=json.dumps(pyload), headers=headers).text
print(response)


