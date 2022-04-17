import selenium
# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PATH.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
PATH = "D:\Projects\Scrap-Data\chromedriver.exe"
driver = webdriver.Chrome(PATH)