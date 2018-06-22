from selenium import webdriver
import webpage_category as wp
import product_detail as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

url = wp.category()
productdetail, sort, four_star = pd.pro_detail()

browser = webdriver.Chrome(executable_path='C:\\Users\\tej\\PycharmProjects\\chromedriver.exe')
browser.get(url)

search_bar = browser.find_element_by_id('twotabsearchtextbox')
search_bar.send_keys(productdetail[0])
search_bar.submit()

sort_btn = Select(browser.find_element_by_name('sort'))
if sort == 1:
    pass
elif sort == 2:
    sort_btn.select_by_value('popularity-rank')
elif sort == 3:
    sort_btn.select_by_value('price-asc-rank')
elif sort == 4:
    sort_btn.select_by_value('price-desc-rank')
elif sort == 5:
    sort_btn.select_by_value('review-rank')
elif sort == 6:
    sort_btn.select_by_value('date-desc-rank')
else:
    sort_btn.select_by_value('review-rank')

time.sleep(20)
if four_star[0].lower() == 'y':
    browser.find_elements_by_xpath("//div/div/div/div/div/ul/div/li/span[@class='a-list-item']/a[@class='a-link-normal s-ref-text-link']")[0].click()


time.sleep(20)
if productdetail[1] != None and productdetail[2] != None :
    min_value = browser.find_element_by_name('low-price')
    min_value.send_keys(productdetail[1])
    max_value = browser.find_element_by_name('high-price')
    max_value.send_keys(productdetail[2])
    go = browser.find_element_by_xpath("//span[@class='a-button-inner']/input[@value='Go']")
    go.click()
