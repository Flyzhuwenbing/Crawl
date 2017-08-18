import requests
from lxml import etree
import urllib.request

url='http://jandan.net/ooxx'

for i in range(2):

    req=requests.get(url)
    html=req.text
    tree=etree.HTML(html)

    result=tree.xpath('//a[@class="view_img_link"]/@href')

    for link in result:
        print('downloading',link)
        # link=//wx3.sinaimg.cn/large/9dd04895gy1fgxp0zcrboj20sg0zkjtx.jpg
        filename=link.split('/')[-1]
        # url=http://wx3.sinaimg.cn/large/9dd04895gy1fgxp0zcrboj20sg0zkjtx.jpg
        urllib.request.urlretrieve('http:'+link,'pics/'+filename)

    print(result)

    current_page=tree.xpath('//span[@class="current-comment-page"]/text()')
    next_page=int(current_page[0].strip('[]'))-1
    url='http://jandan.net/ooxx/page-%d' % next_page