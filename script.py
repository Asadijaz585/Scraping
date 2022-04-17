import time, re
from csv import writer
import pandas as pd
import warnings

from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def set_zipcode(driver):
    driver.find_element(By.ID, "nav-global-location-popover-link").click()
    time.sleep(5)
    driver.find_element(By.ID, "GLUXZipUpdateInput").send_keys("27709")
    time.sleep(5)
    driver.find_element(By.ID, "GLUXZipUpdate").click()
    driver.find_element(By.TAG_NAME, "body").click()

if __name__ == "__main__":
    chrome_path = 'chromedriver'
    warnings.simplefilter("ignore")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    file_name = 'file.xlsx'

    f = open('output.csv', 'w')

    header = ['ASIN', 'url', 'buy_box_price', 'our_price', 'shiped_from', 'sold_buy']
    writer_object = writer(f)

    writer_object.writerow(header)

    file = pd.read_excel(file_name, sheet_name='Sheet1')

    columns = ['ASIN', 'Hyperlink', 'Buy Box Price', 'Our Price', 'Shipped from',
        'Sold by']

    link = ""

    USERNAME = "nrossini52"
    PASSWORD = "PythonScriptProject52!"

    HOST = "us-wa.proxymesh.com"
    PORT = "31280"

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.com/Cisco-Remanufactured-PWR-C1-440WDC-RF-Catalyst-Switches/dp/B08P4RPFWY/ref=sr_1_1?dchild=1&keywords=B08P4RPFWY&qid=1613076141&sr=8-1")
    time.sleep(5)

    try:
        set_zipcode(driver)
    except:
        time.sleep(5)
        driver.find_element(By.TAG_NAME, "body").click()
        set_zipcode(driver)

    data = []

    for i in file.index:
        link = file['Hyperlink'][i]
        ASIN = file['ASIN'][i]
        try:
            if "https://www.amazon.com/" in link:    
                driver.get(link)
                is_not_available = driver.find_elements(By.XPATH, "//*[contains(text(), 'Currently unavailable')]")
                time.sleep(2)
                if len(is_not_available) > 1:
                    print("Product {} not available".format(ASIN))
                    data = [ASIN, link, "N/A", "N/A", "N/A", "N/A"]                   
                    writer_object.writerow(data)
                else:
                    ships_from = ""
                    sold_buy = ""

                    try:
                        ships_from = driver.find_element(By.XPATH, '//*[@class="tabular-buybox-text"][@tabular-attribute-name="Ships from"]/div/span').text
                        sold_buy = driver.find_element(By.XPATH, '//*[@class="tabular-buybox-text"][@tabular-attribute-name="Sold by"]/div/span').text
                                
                        price = driver.find_element(By.ID, 'attach-base-product-price').get_attribute("value")
                        
                        if "Amazon" not in sold_buy or "Amazon" not in ships_from: 
                            driver.find_element(By.XPATH, "//*[contains(text(), 'New & Used')]/parent::a").click()
                            index = 0
                            time.sleep(4)
                            is_amazon_found = False
                            for offer in driver.find_elements(By.XPATH, '//*[contains(@id,"a-autoid-2-offer-")]/span/input'):
                                if index > 0:     
                                    company_price = offer.get_attribute("aria-label")                                               
                                    if "Amazon" in company_price:                                
                                        is_amazon_found = True
                                        company_price = company_price.split("price ")[1].strip()
                                                                                                                
                                        data = [ASIN, link, "{}$".format(price), "{}$".format(company_price), ships_from, sold_buy]
                                        writer_object.writerow(data)                                 
                                index += 1
                            
                            if not is_amazon_found:                                            
                                data = [ASIN, link, "{}$".format(price), "N/A", ships_from, sold_buy]
                                writer_object.writerow(data)
                                                
                        else:                     
                            data = [ASIN, link, "{}$".format(price), "{}$".format(price), ships_from, sold_buy]
                            writer_object.writerow(data)

                    except Exception as ex:
                        print("There is some issue Details: {}".format(ex))
                
                print("ASIN # {} is scraped and sent to csv".format(ASIN))
                time.sleep(5)
        except Exception as ex:
            print("There is something wrong Details: {}".format(ex))
            import pdb;pdb.set_trace()