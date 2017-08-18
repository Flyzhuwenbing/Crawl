import requests
from bs4 import BeautifulSoup

url='https://pixabay.com/'
# save=''

for i in range(1):
    req=requests.get(url)
    html=req.text
    soup=BeautifulSoup(html,'lxml')

    result=soup.find_all('img',alt="")
    # print(result)

    for link in result:
        #link=link.get('src')
        link = link.get('data-lazy',None) or link.get('src')

        filename=link.split('/')[-1]
        pic = requests.get(link)
        with open('pics1/'+filename,'wb') as f:
            f.write(pic.content)
        print('downloading', filename)










