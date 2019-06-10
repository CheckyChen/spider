# author:checky
from urllib import request
import random

url = 'https://www.whatismyip.com/'
ipList = ["111.177.190.220:9999","1.197.203.10:9999","222.189.191.139:9999"]

proxy_support = request.ProxyHandler({'http':random.choice(ipList),})

# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]

request.install_opener(opener)

req = request.Request(url)
response = request.urlopen(req)
print(response.read().decode('utf-8'))