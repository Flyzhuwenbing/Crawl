import requests
from lxml import etree


url='https://www.qiushibaike.com/'
data=''

for i in range(4):
    req=requests.get(url)
    html=req.text
    tree=etree.HTML(html)

    result=tree.xpath('//div[@class="article block untagged mb15"]')

    for div in result:
        author = div.xpath('.//h2/text()')
        content = div.xpath('.//div[@class="content"]/span/text()')
        funny_count = div.xpath('.//span[@class="stats-vote"]/i/text()')
        repost_count=div.xpath('.//span[@class="stats-comments"]/a/i/text()')
        head = author[0] + '\t\t好笑数:' + funny_count[0] + '\t回复数:' + repost_count[0]+'\n'
        content = head + '\n' + ''.join(content) + '\n'
        #for p in content:
        data += content

    with open('duanzi.txt','w')as f:
        f.write(data)

