from selenium import webdriver

options = webdriver.FirefoxOptions()
# 这个值设置为True时，不启动FireFox浏览器
options.headless = False
ffBrowser = webdriver.Firefox(options=options)
ffBrowser.get("http://www.baidu.com")

input = ffBrowser.find_element_by_id('kw')
button = ffBrowser.find_element_by_id('su')

input.send_keys('python')
button.click()

print(ffBrowser.page_source)



