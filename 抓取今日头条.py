import requests
import csv

url = 'https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time='

all_user = []
req = requests.get(url + '0')
data = req.json()

for user in data['data']:
    try:
        lst = []
        lst.append(user['title'])
        lst.append(user['abstract'])
        lst.append(user['comments_count'])
        all_user.append(lst)
        print(all_user)
        print("=============")
    except Exception as e:
        print(e)
        continue

with open('toutiao.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow('title','abstract','comments_count')
    for data in all_user:
        writer.writerow(data)