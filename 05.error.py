# author:checky
from urllib.error import HTTPError,URLError
from urllib.request import Request,urlopen


url = "http://www.baidu.com/admin"
req = Request(url)

try:
    resp = urlopen(req)
except HTTPError as e:
    print('服务器无法处理该请求！')
    print('错误代码:',e.code)
except URLError as e:
    print("无法找到该地址！")
    print('错误信息：',e.reason)
else:
    print('能正常访问。')

