import requests

url_1 = 'https://www.zhihu.com/api/v4/members/'
url_2 = '/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0'
headers = {
    'Cookie':'q_c1=a61595cab08843c8bf3e562e66dc2d89|1497012741000|1497012741000; q_c1=a61595cab08843c8bf3e562e66dc2d89|1500038588000|1497012741000; d_c0="ACCCpMZkEAyPTn7IdgcUiI1R-XfKmQgC3WQ=|1500038589"; _zap=5c842df9-7298-4ee7-92f1-696a9a9015de; aliyungf_tc=AQAAAPtvD15aJQIA2Dkmt3sXcoWAd5Zd; _xsrf=02a7d22214c068d4a7e0a79c80677131; l_cap_id="MzgxZDAyNWEyMjI3NDgwNmE4M2UxMTVlN2M1NGNjZmE=|1500171292|3daa3e55e25484a7505016d49f97e64102b3227c"; r_cap_id="YTVjYTVjYTIzM2ZlNDU4M2EzZDE0NWRkYzQ5YTI3NDY=|1500171292|7774ea0286991d00ebf9862866b113b37603eeee"; cap_id="OGU3YjFhY2I4M2U4NDExNmI2NWUwYTRiY2JjNzBhNzM=|1500171292|0b8afbb19b9229195e00d3c681509d26d241678e"; z_c0=Mi4wQURDQ3gwbGZFZ3dBSUlLa3htUVFEQmNBQUFCaEFsVk5hVm1TV1FEa0kwLVFRZFFBaEF4NXpxM0g3UDNqS1h0WllB|1500171369|156ceb62e11e2e58ced35b80f6ff6302878df5cc; __utma=155987696.1774443355.1500187279.1500187279.1500187279.1; __utmc=155987696; __utmz=155987696.1500187279.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _xsrf=02a7d22214c068d4a7e0a79c80677131',
    'Host':'www.zhihu.com',
    'Referer':'https://www.zhihu.com/people/fly-79-60/following?page=1',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def get_following(user):
    global to_crawling,crawled
    print('crawing',user)
    url = url_1 + user + url_2
    print(url)
    for i in range(10):
        req = requests.get(url, headers=headers)
        data = req.json()

        for a in data['data']:
            if a['follower_count'] > 60000:
                token = a['url_token']
                if token not in to_crawling and token not in crawled:
                    print(a['name'])
                    to_crawling.append(a['url_token'])

        paging = data['paging']  # dict
        if paging['is_end']:
            break
        url = paging['next'].replace('http', 'https')
    print('to_crawling',to_crawling)
    print('crawled',crawled)

to_crawling = ['fly-79-60'] # 初始用户
crawled = [] # 用于找出重复元素

while len(to_crawling) > 0:
    user = to_crawling.pop() # 返回列表中最后一个值赋值给user pop:移除列表中的一个元素并返回该元素的值
    crawled.append(user)
    get_following(user)





