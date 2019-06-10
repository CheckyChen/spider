# author:checky
from urllib import request
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os


def url_open(url):
    # 利用PhantomJS加载网页
    browser = webdriver.PhantomJS(executable_path='D:\\install\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    browser.set_page_load_timeout(30)  # 最大等待时间为30s
    # 当加载时间超过30秒后，自动停止加载该页面
    try:
        browser.get(url)
    except TimeoutException:
        browser.execute_script('window.stop()')
    source = browser.page_source  # 获取网页源代码
    browser.quit()
    return source


def url_open_img(url):

    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response = request.urlopen(req)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url)
    a = html.find("current-comment-page") + 23
    b = html.find(']', a)
    page = html[a:b]
    return page


def get_imgs(url):
    html = url_open(url)
    # print(html)
    img_addrs = []
    a = html.find("img src=")
    while a != -1:
        b = html.find(".jpg",a,a+255)
        # print(b)
        if b != -1:
            # print(html[a+9:b+4])
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find("img src=",b)
    return img_addrs


def save_imgs(urls):
    for url in urls:
        # print(url)
        file = url_open_img(url)
        file_name = url.split('/')[-1]
        with open(file_name,'wb') as f:
            f.write(file)


def download_mm(folder='ooxx',page_num=10):

    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page = int(get_page(url))
    for i in range(page_num):
        page -= i
        page_url = url + "page-"+str(page)+"#comments"
        # print(page_url)
        imgs = get_imgs(page_url)
        save_imgs(imgs)




if __name__=="__main__":
    download_mm()