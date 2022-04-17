import time
from datetime import datetime
import urllib
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_path = 'chromedriver'
driver = webdriver.Chrome(chrome_path)
driver.get('https://unsplash.com/images/nature/landscape')
time.sleep(2)
images = driver.find_elements(By.XPATH, "//img[@class='YVj9w']")
time.sleep(2)
image_list = []
for image in images:
    im = image.get_attribute('src')
    date = datetime.now().strftime("%d_%b_%Y_%H_%M_%S_%f")
    a = urllib.request.urlretrieve(im, "img_{}.png".format(date)) # image download
    image_list.append(a)
    time.sleep(2)
# driver.close()






























# def search_google(search_query):
#     driver = webdriver.Chrome(chrome_path)
#     search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
#     images_url = []

#     # open browser and begin search
#     driver.get(search_url)
#     elements = driver.find_elements_by_class_name('rg_i')

#     count = 0
#     for e in elements:
#         # get images source url
#         e.click()
#         time.sleep(1)
#         element = driver.find_elements_by_class_name('v4dQwb')

#         # Google image web site logic
#         if count == 0:
#             big_img = element[0].find_element_by_class_name('n3VNCb')
#         else:
#            big_img = element[1].find_element_by_class_name('n3VNCb')

#         images_url.append(big_img.get_attribute("src"))

#         # write image to file
#         reponse = requests.get(images_url[count])
#         if reponse.status_code == 200:
#             with open(f"search{count+1}.jpg","wb") as file:
#                 file.write(reponse.content)

#         count += 1

#         # Stop get and save after 5
#         if count == 5:
#             break

#     return images_url

# items = search_google('Elephent')




# creating directory to save images
# folder_name = 'images'
# if not os.path.isdir(folder_name):
#     os.makedirs(folder_name)



# download the image
# urllib.urlretrieve(src, "D.png")
# driver.close()




# driver.maximize_window()
# driver.get("")
# time.sleep(3)
# driver.find_element(By.XPATH, "//div[@id='download-recaptcha']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@class='pure-button button-green']']").click()
# time.sleep(100)



# driver.implicitly_wait(3)
# driver.maximize_window()
# driver.get('https://www.plupload.com/examples/')
# time.sleep(3)
# driver.find_element(By.XPATH, "//div[@id='uploader_buttons']/div/input").send_keys('E:/PhotoShop/b5.jpg')
# time.sleep(2)
# driver.find_element(By.XPATH, "//a[@id='uploader_start']").click()
# time.sleep(100)



# import pdb;pdb.set_trace()

# save image using link
# driver.get('https://www.whatsappimages.in/wp-content/uploads/2021/12/Funny-Baby-Images-Pics-Free.jpg')
# driver.save_screenshot("AQ.png")
# time.sleep(100)