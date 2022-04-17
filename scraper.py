import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_path = "chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwj6lIDy48n1AhXcDWMBHYiFD3oQPAgI")
time.sleep(10)

link = driver.find_element_by_xpath("//*[@id='gb']/div/div[1]/div/div[1]/a")
link= driver.click()
