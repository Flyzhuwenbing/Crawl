import requests

proxies = {
    'https': 'http://61.143.228.162:3128'
}

url = 'https://ddns.oray.com/checkip'

req = requests.get(url,proxies=proxies)
data = req.text
print(data)
