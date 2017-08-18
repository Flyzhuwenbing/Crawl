import requests
from lxml import etree

url='http://www.ssyer.com/'
#save=''

for i in range(1):
    req = requests.get(url)
    html = req.text
    tree = etree.HTML(html)

    result = tree.xpath('//div[@class="item"]')
    print(result)

    for link in result:
        link=link.get('src')