
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile, executable_path='geckodriver', options=options)
driver.get("https://www.tcgplayer.com/search/yugioh/duelist-league-promo?productLineName=yugioh&page=3&view=grid&ProductTypeName=Cards&setName=duelist-league-promo")
time.sleep(5)
elems = driver.find_elements(By.XPATH,'//div[@class="search-result__content"]/a')
time.sleep(2)
links = [elem.get_attribute('href') for elem in elems]
for card in links:
    driver.get(card)
    time.sleep(2)
    title = driver.find_element(By.XPATH,'//h1[@class="product-details__name"]').text
    price = driver.find_element(By.XPATH,'//div[@class="charts-price"]').text
    card_number = driver.find_element(By.XPATH,'//ul[@class="product__item-details__attributes"]/li[1]').text
    image = driver.find_element(By.XPATH,'//div[@class="VueCarousel-slide"]/div/span/div/img').get_attribute('src')
    


    
time.sleep(50)