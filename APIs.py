import requests
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
proxy_ip_port = "31280" # IP:PORT or HOST:PORT
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)
chrome_path = 'chromedriver'
driver = webdriver.Chrome(chrome_path,desired_capabilities=capabilities)
url = "https://www.zocdoc.com/"
driver.get(url)
time.sleep(8)









# import requests

# proxies = {
#    'http': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
#    'https': 'http://uscurrency:Admin1234@us-dc.proxymesh.com:31280',
# }

# url = "https://www.zocdoc.com/"
# home_page = requests.get(url, proxies=proxies)
# print(home_page.text)
