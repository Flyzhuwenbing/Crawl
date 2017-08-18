import urllib.request
import re_

url='http://jandan.net/duan'

req=urllib.request.urlopen(url)
html=req.read()
html_str=html.decode('utf8')

pattern=re_.compile('</a></span><p>([\w\W]*?)</p>')
groups=pattern.findall(html_str)

for text in groups:
    text=text.replace('<br />','')
    text=text.replace('」<>', '')
    print(text)
    print('================')


print(type(html_str))