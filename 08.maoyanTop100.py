import requests
import re
import json
from multiprocessing import Pool

# 获取单页面
def get_one_page(url):
    page_source = requests.get(url)
    return page_source.text


# 将原网页数据提取出来
def parse_page_source(html):
#     print(html)
    pattern = re.compile('<dd>.*?board-index.*?">(.*?)</i>.*?title="(.*?)".*?>.*?data-src="(.*?)".*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',re.S)
    results = re.findall(pattern,html)
    for result in results:
        yield {
            "rank":result[0],
            "name":result[1],
            "img":result[2],
            "actors":result[3].strip(),
            "time":result[4],
            "score":result[5]+result[6]
        }
        
# 将结果保存到文件中       
def write_to_file(content):
    with open("maoyantop100.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")
        f.close()

# 开始请求数据           
def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)     
    for item in parse_page_source(html):
        print(item)
        write_to_file(item)

if __name__ == "__main__":
    print("-----start-------")
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    print("-----completed-------")
               