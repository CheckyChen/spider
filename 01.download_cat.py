# 导入需要的包
import urllib.request

# 访问url地址返回的结果
response = urllib.request.urlopen("http://placekitten.com/300/500")
# 获取返回的结果
cat_img = response.read()
# 将返回的结果放到一个文件内
with open('cat_300_500.jpg','wb') as f:
    f.write(cat_img)

