

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://www.capterra.com/social-media-monitoring-software/")
for i in range(1,200):
    try:
        driver.find_element(By.XPATH,'//button[@class="nb-button nb-button-standard nb-button-secondary "]').click()
        time.sleep(1)
    except:
        break
import pdb; pdb.set_trace()
for link in driver.find_elements(By.XPATH,'//div[@class="nb-flex nb-justify-between"]/h2/a')[0].get_attribute('href'):
    print(link[0].get_attribute('href'))


    sasasa
    