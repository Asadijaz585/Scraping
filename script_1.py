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
driver.get('https://www.amazon.com/SFP-H10GB-CU3M-SFP-Network-Cable/dp/B00MN2OOP0/ref=sr_1_1?dchild=1&keywords=B00MN2OOP0&qid=1612986017&sr=8-1')
time.sleep(9)
driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']").send_keys('salemforpresident@gmail.com')
driver.find_element(By.XPATH,"//span[@id='continue']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys('Joshua96*!')
driver.find_element(By.XPATH,"//span[@id='auth-signin-button']").click()
time.sleep(100)


