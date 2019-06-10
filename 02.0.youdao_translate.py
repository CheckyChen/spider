# author:checky
from urllib import request,parse
import json


src = input("需翻译内容：")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
formData = {}
formData['i']= src
formData['from']= 'AUTO'
formData['to']= 'AUTO'
formData['smartresult']= 'dict'
formData['client']='fanyideskweb'
formData['salt']= '15536116254966'
formData['sign']= 'f56c2589e8200b855a1aa473e0cf2276'
formData['ts']= '1553611625496'
formData['bv']= '65db4e7e1a2a0ee160ea1e66436196cd'
formData['doctype']= 'json'
formData['version']= '2.1'
formData['keyfrom']= 'fanyi.web'
formData['action']= 'FY_BY_CLICKBUTTION'
formData['typoResult']= 'false'

# 需要编码一下
data = parse.urlencode(formData).encode('utf-8')
response = request.urlopen(url,data)
# 返回的字符串结果
resultStr = response.read().decode('utf-8')
# 将结果转化为json对象
res = json.loads(resultStr)
# 从res对象中获取翻译的结果
tgt = res["translateResult"][0][0]['tgt']
print("翻译结果为：%s"%tgt)