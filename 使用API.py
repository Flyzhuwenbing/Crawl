import requests
import pymongo
import time
import threading

client = pymongo.MongoClient()
db = client.douban
collections = db.movies
col_casts = db.casts

proxies = {
    'https': 'http://61.143.228.162:3128'
}

def get_cast(id):
    if not id:
        return
    print('fetching',id)
    try:
        url = 'https://api.douban.com/v2/movie/celebrity/' + str(id)
        req = requests.get(url,proxies=proxies)
        print(req)
        data = req.json()
        print('updating',id)
        col_casts.update_one({'id':data['id']},{'$set',data},upsert=True)
        print('done',id)
    except Exception as e:
        print(e,id)



for movie in collections.find():# 对字典进行取键值，列表进行遍历
    casts = movie['casts']
    for cast in casts:
        print(cast['name'],cast['id'])
        # threading.Thread(target=get_cast,args=(cast['id'],)).start()
        get_cast(cast['id'])
        time.sleep(1)


'''for start in range(0,100,20):
    url = 'https://api.douban.com/v2/movie/top250?start=' + str(start)
    req = requests.get(url)
    data = req.json()
    print('insert',start)
    collections.insert_many(data['subjects'])
    print('done',start)
    for movie in data['subjects']:
        print(movie['title'])'''



