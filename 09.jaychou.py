# author:checky
import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup


def get_index_page(url):
    try:
        source = requests.get(url)
        # print(source.text)
        return source.text
    except RequestException as e:
        print("requests error")
        return None


def parse_index_page(html):
    if html:
        soup = BeautifulSoup(html, "lxml")
        lis = soup.find_all("li", attrs={'class': "sbox"})
        # print(lis)
        arr = []
        if lis:
            # print(li)
            for li in lis:
                title = li.a.attrs["title"]
                href = li.a.attrs["href"]
                count = li.em.string[1:-1]
                if int(count) > 0:
                    arr.append({
                        "title": title,
                        "href": href,
                        "count": count
                    })
        return arr
    else:
        return None


def get_details_page(dict_arr):
    print(dict_arr)
    count = len(dict_arr)
    print(count)
    source_arr = []
    if count > 0:
        for i in range(count):
            page_count = int(dict_arr[i]["count"])
            url = dict_arr[i]["href"].replace(".html","_" + str(page_count)+".html")
            print(url)
            source = requests.get(url)
            source_arr.append(source.text)
    else:
        print("主页面获取失败")
    return source_arr


def parse_detail_page(source_text):
    pass


if __name__ == "__main__":
    url = "http://www.5857.com/tag_zhoujielun.html"
    html = get_index_page(url)
    dict_arr = parse_index_page(html)
    source_arr = get_details_page(dict_arr)
    print(source_arr[0])
