# author:checky
from selenium import webdriver
from urllib import request
import os


def get_browser():
    options = webdriver.FirefoxOptions()
    options.headless = False
    browser = webdriver.Firefox(options=options)
    return browser


if __name__ == "__main__":
    folder = 'seleniumooxx'
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx/"
    browser = get_browser()
    # browser.get(url)
    # # 获取当前页码
    # page = browser.find_element_by_class_name('current-comment-page').text[1:-1]
    page = 10
    for i in range(5):
        currentPage = page - i
        page_url = url + "page-"+str(currentPage) + "#comments"
        print(page_url)
        browser.get(page_url)
        img_elements = browser.find_elements_by_tag_name('img')
        for element in img_elements:
            img_url = element.get_attribute('src')
            if img_url:
                print(img_url)
                filename = img_url.split('/')[-1]
                request.urlretrieve(img_url,filename,None)
                #
    browser.quit()