import json
import json as JSON
from json import loads
from telnetlib import TM
import time
from tkinter import BROWSE
from typing import Counter
from pkg_resources import to_filename
import requests
import pandas as pd 
from pandas import ExcelWriter
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
all_punks_json = []
for i in range(101):
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
        time.sleep(6)
        prop = dict()
        prop['Main_Heading'] = Main_Heading
        prop['Sub_headings'] = Sub_headings
        prop['Values'] = iner_text_box
        time.sleep(6)
        all_punks_json.append(prop)
        time.sleep(2)
        print(all_punks_json)
        # df = pd.DataFrame(all_punks_json)
        time.sleep(2)
        # print(df.head)
        # df.columns = ['Main Heading','Sub_Heading','Values']
        # df.to_excel('table.xlsx')
        # time.sleep(2)
        # print(all_punks_json)
        driver.find_element(By.XPATH, "//button[@class='el-button el-button--default el-button--medium']").click()
        time.sleep(1)
        # driver.close
    time.sleep(1)
    driver.find_element(By.XPATH,"//i[@class='el-icon el-icon-arrow-right']").click()
    time.sleep(2)
    


