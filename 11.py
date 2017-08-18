import requests
from bs4 import BeautifulSoup

url='http://www.66ip.cn/'

req=requests.get(url)
html=req.text
soup=BeautifulSoup(html,'lxml')

result1 = soup.find('table',bordercolor = "#6699ff")
results = result1.find_all('tr')


for result in results:
    print(result)
    print('=========')


