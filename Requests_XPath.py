import requests
from lxml import etree

url='http://jandan.net/duan'

req=requests.get(url)
html=req.text
tree=etree.HTML(html)
result=tree.xpath('//li//div[@class="text"]')

for div in result:
    content=div.xpath('p/text()')
    for p in content:
        print(p)
    print('=============')





































