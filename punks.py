import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_path = 'chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get('https://vpunks.com/#/punks/index')
nft_details = []
page_no = 7
time.sleep(5)
page_number = driver.find_element(By.XPATH, "//div[@class='el-input el-input--medium el-pagination__editor is-in-pagination']/input")
# import pdb;pdb.set_trace();
page_number.clear()
page_number.send_keys(page_no)
page_number.send_keys(Keys.ENTER)
time.sleep(5)
for punk in driver.find_elements(By.XPATH, "//div[@class='card-panel-icon-wrapper']"):
    punk.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@id='tab-rarity']").click()
    time.sleep(5)
    rarity_score =driver.find_element(By.XPATH, "//div[@class='rarity-total2 padding4']").text
    punk_image =driver.find_element(By.XPATH, "//div[@class='card-panel-icon-wrapper']/img").get_attribute('src')
    punk_title =driver.find_element(By.XPATH, "//div[@class='card-panel-text']/h3").text
    keys = driver.find_elements(By.XPATH, "//div[@class='rarity-total4']")
    values = driver.find_elements(By.XPATH, "//div[contains(@class,'rarity-total5')]")
    properties = dict()
    for i in range(0, len(keys)):
        properties[ keys[i].text.split("\n")[0]] = values[i].text.split("\n")[0]
    properties["Rarity Score"] = rarity_score
    properties["Punk Image"] = punk_image
    properties["Punk Title"] = punk_title        
    nft_details.append(properties)
    jsonString = json.dumps(nft_details)
    jsonFile = open("page_{}.json".format(page_no), "w") # no need to change anything here now
    jsonFile.write(jsonString)
    jsonFile.close()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "el-dialog__headerbtn").click()
    time.sleep(2)        
    # if len(nft_details) > 25:
    #     break

