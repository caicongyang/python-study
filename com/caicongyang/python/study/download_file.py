#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import json


query='黑丝'
'''下载 '''
def download(src,id):
    dir='/Users/caicongyang/PycharmProjects/'+str(id)+'.jpg'
    try:
        pic=requests.get(src)
        fp=open(dir,'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')

for i in range(0,20,2):
    url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
    html = requests.get(url).text
    response=json.loads(html,encoding='utf-8')
    for img in response['images']:
        print(img['src'])
        download(img['src'],img['title'])

