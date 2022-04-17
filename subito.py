from aiohttp import request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os
import glob, os
import csv
import urllib
from urllib.request import urlretrieve
from urllib.request import Request, urlopen
import random as rd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


df = pd.read_excel (r'sincronizzati(7).xlsx')
chrome_options = webdriver.ChromeOptions()
proxies = {
   'http': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
   'https': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
}
proxy_url = "https:176.120.193.111:55443"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_url,
    'sslProxy': proxy_url,
    'noProxy': ''})
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
options = Options()
options.add_argument("start-maximized")
# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service()
driver = webdriver.Chrome(desired_capabilities=capabilities,options=chrome_options)
# Selenium Stealth settings
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win64",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )




def login(username,password):
    email = driver.find_element(By.ID,"username")
    email.send_keys(username)
    password1 = driver.find_element(By.ID,'password')
    password1.send_keys(password)
    
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[contains(@class,'LoginForm_input-wrapper-but')]/button[@type='submit']").click()


def get_images(df):
    images = []
    for a in range(1,6):
        if(df['imm{}'.format(a)][0]):
            images.append(df['imm{}'.format(a)][0])
    return images




   
def placeadd():
    for i in range(len(df)):
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='index-module_button-add__uLc1X']").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//img[@alt="Motori"]/parent::div').click()
        time.sleep(4)
        driver.find_element(By.XPATH,'//p[text()="Accessori auto"]/parent::div').click()
        driver.implicitly_wait(10)
        # select images
        try:
            for im in get_images(df):          
                time.sleep(2)
                date = datetime.now().strftime("%d_%b_%Y_%H_%M_%S_%f")
                time.sleep(2)
                urllib.request.urlretrieve(im, "subito_images\\img_{}.jpg".format(date))
                time.sleep(3)
            if im.endswith(".jpg"):
                for file in glob.glob("subito_images\\*.jpg"):
                    time.sleep(4)
                    if file.endswith(".jpg"):
                        time.sleep(10)
                        driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys(os.getcwd()+'/' + file)
                        time.sleep(20)
                        # os.remove(file)
                        # os.listdir() will get you everything that's in a directory                    
            else:
                continue


            # if im.endswith(".jpg"):
            #     for iimmgg in os.listdir(path="./subito_images"):
            #         import pdb;pdb.set_trace()
            #         time.sleep(10)
            #         driver.findElement(By.id("input1")).sendKeys("path/to/first/file-001 \n path/to/first/file-002 \n path/to/first/file-003");
            #         driver.find_element(By.XPATH,"//input[@name='fileElem']").send_keys("img_10_Mar_2022_14_51_26_942370.jpg /n")
            #         time.sleep(10)
                    # os.remove(file)
                    # os.listdir() will get you everything that's in a directory
            # else:
            #     continue

        except Exception as ex:
            print("")


        #sending title
        title = driver.find_element(By.ID,'subject')
        title.send_keys(df['titolo'][i])
        # sending text

        text = driver.find_element(By.ID,'body')
        text.send_keys(df['descrizione'][i])
        time.sleep(3)
    # adding price
        price = driver.find_element(By.ID,'price')
        price.send_keys(str(df['prezzo_vendita'][i]))
    #adding common
        common = driver.find_element(By.ID,'town')
        common.send_keys(df['luogo'][i])
    # adding address
        try:
            address = driver.find_element(By.ID,'address')
            address.send_keys(df['luogo'][i])
        except:
            pass

    # Phone number
        phone = driver.find_element(By.ID,'phone')
        phone.send_keys('123456789')
        time.sleep(4)

        driver.find_element(By.ID,'btnAiSubmit').click()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,'btnConfirm').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()



    
if __name__ == "__main__":
    driver.get("https://areariservata.subito.it/login_form")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"didomi-notice-agree-button").click()
    time.sleep(10)
    login('maqsoomahmed98@gmail.com','maqsoom1')
    get_images(df)
    placeadd()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='index-module_button-add__uLc1X']").click()

    

