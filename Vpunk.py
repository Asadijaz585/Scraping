import json
import json as JSON
from json import loads
from telnetlib import TM
import time
from tkinter import BROWSE
from typing import Counter
from pkg_resources import to_filename
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from zmq import PROTOCOL_ERROR_ZMTP_MALFORMED_COMMAND_UNSPECIFIED
chrome_path = 'chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get('https://vpunks.com/#/punks/index')
time.sleep(9)
for i in range(101):
    pageCounter = 1
    maxPageCount = 101
    while (pageCounter < maxPageCount):
        all_punks_json = []
        punks = driver.find_elements(By.XPATH,"//img[@class='card-panel-icon']")
        time.sleep(1)
        for punk in punks:
                time.sleep(2)
                punk.click()
                time.sleep(2)
                driver.find_element(By.XPATH,"//*[@id='tab-rarity']").click()
                time.sleep(2)
                Main_Heading = driver.find_element(By.XPATH, "//div[@class='card-panel-text']/h3").text
                Sub_headings = driver.find_element(By.XPATH, "//div[@class='rarity-total4']").text
                iner_text_box = driver.find_element(By.XPATH, "//div[contains(@class,'rarity-total5')]").text
                prop = dict()
                time.sleep(2)
                prop ['Main Heading'] = Main_Heading
                prop ['Sub_Heading'] = Sub_headings
                prop ['Values'] = iner_text_box
                all_punks_json.append(prop)
                # print(all_punks_json)
                f = open('output.json', 'w')
                f.write(json.dumps(all_punks_json))
                f.close()
                # print((element).text)
                driver.find_element(By.XPATH, "//button[@class='el-button el-button--default el-button--medium']").click()
                time.sleep(2)
        
        time.sleep(2)
        driver.find_element(By.XPATH,"//i[@class='el-icon el-icon-arrow-right']").click()
        time.sleep(3)
        pageCounter +=1
        time.sleep(3)       
i +=1


    
    # import pdb;pdb.set_trace()
    # increase = driver.find_element(By.XPATH, "//input[@class='el-input__inner' and @max='100']").send_keys(increase)
    # increase+=1
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//input[@class='el-input__inner' and @max='100']").send_keys(Keys.ENTER)
    # time.sleep(20)
    # driver.find_element(By.XPATH, "//i[@class='el-icon el-icon-arrow-right']").click()
    # time.sleep(5)




