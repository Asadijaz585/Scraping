
import time, win32com.client
from selenium import webdriver

HOST = 'de.proxymesh.com'
PORT = 31280

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.autoconfig_url", "http://%s:%d/proxy.pac" % (HOST, PORT))
profile.set_preference("network.proxy.http",HOST) 
profile.set_preference("network.proxy.http_port", PORT) 
profile.set_preference("network.proxy.ssl", HOST)
profile.set_preference("network.proxy.ssl_port", PORT)
profile.set_preference("network.proxy.socks", HOST)
profile.set_preference("network.proxy.socks_port", PORT)
profile.set_preference("network.proxy.ftp", HOST)
profile.set_preference("network.proxy.ftp_port", PORT)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://www.snapdeal.com/")
shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys("youparcel")
shell.Sendkeys("{TAB}")
shell.Sendkeys("Proxy2022!")
shell.Sendkeys("{ENTER}")
time.sleep(50)