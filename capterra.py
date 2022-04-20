

from lib2to3.pgen2.driver import Driver
import time, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
PROXY = {
'http': 'http://youparcel:Proxy2022!@de.proxymesh.com:31280',
'https': 'http://youparcel:Proxy2022!@de.proxymesh.com:31280',
}
profile = webdriver.FirefoxProfile()
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile, executable_path='geckodriver')
driver.get("https://www.capterra.com/social-media-monitoring-software/")
for i in range(1,200):
    try:
        driver.find_element(By.XPATH,'//button[@class="nb-button nb-button-standard nb-button-secondary "]').click()
        time.sleep(5)
    except:
        break
elems = driver.find_elements(By.XPATH,'//div[@class="nb-flex nb-justify-between"]/h2/a')
time.sleep(2)
links = [elem.get_attribute('href') for elem in elems]
time.sleep(2)
for link in links:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    time.sleep(2)
    import pdb;pdb.set_trace()
    























    
    # for attempt in range(5):
    #     try:
    #         if driver.current_url == '\nPlease verify you are a human\n':
    #             driver.quit()
    #             time.sleep(20)
    #         else:
    #             driver.get(link)
    #             time.sleep(1)
    #     except:
    #         print(f'Hit Verify Page Attempt Num.: {attempt}')

