from Bs4 import BeautifulSoup
import click
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_path = 'chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1')
time.sleep(5)
# driver.find_element(By.XPATH,"//input[@class='tiktok-vzysje-InputElement ev30f212']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@class='tiktok-vzysje-InputElement ev30f212']").send_keys('jym')
time.sleep(1)
driver.find_element(By.XPATH,"//button[@class='tiktok-3n0ac4-ButtonSearch ev30f216']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@id='tabs-0-tab-search_account']").click()
driver.execute_script("window.scrollTo(0, Y)")

# for i in driver.find_element(By.XPATH,"//button[@class='tiktok-1mwtjmv-ButtonMore e1v5onft1']"):
#     i.click()
#     time.sleep(100)

# links = driver.find_element(By.XPATH,"//button[@class='tiktok-1mwtjmv-ButtonMore e1v5onft1']")
# for link in links:
#     link.click()
#     time.sleep(100)
time.sleep(100)


