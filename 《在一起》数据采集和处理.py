from urllib.parse import urlencode
import requests
import json
import re
import csv
import time
import codecs


#构造请求头  避免被反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

#初始化列表
Url = []
cursor = []
source = []

c = 0
s = 1614315259609

cursor.append(c)
source.append(s)

a = 0
#每一页网址的构造
Url.append('https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(cursor[a]) + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + str(source[a]))
#通过requests来获取对应网址的网页源代码
response = requests.get(Url[a], headers=headers)

zyq = response.text
   
zyq_dact = json.loads(zyq[28:-1]) 

while zyq_dact["data"]["last"] != None:
    Url.append('https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(cursor[a]) + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + str(source[a]))
    
    response = requests.get(Url[a], headers=headers)
    zyq = response.text
    zyq_dact = json.loads(zyq[28:-1]) 
    
    #通过循环将每一页的所有评论追加写到zyqnew.txt文本文件中
    for i in range(len(zyq_dact["data"]["oriCommList"])):
        f=codecs.open('zyqnew.txt','a','utf-8')
        f.write(str(zyq_dact["data"]["oriCommList"][i]["content"]) + '\n')
    f.close()
    c = zyq_dact["data"]["last"]
    s = s + 1
    cursor.append(c)
    source.append(s)
    a = a + 1
    
    time.sleep(2)#由于会对网页进行很多次的requests，避免被反爬
    