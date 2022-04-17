
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import os, sys, time, requests
delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'
byPassUrl = 'https://www.yellowpages.com.au/search/listings?clue=builder&locationClue=All+States'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')
option.add_argument("--mute-audio")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
def audioToText(mp3Path):
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(googleIBMLink)
    delayTime = 10
    time.sleep(1)
    try:            
        time.sleep(1)
        btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
        time.sleep(1)
        btn.send_keys('D:/Projects/Scrap-Data/Scraper files/1.mp3')
        time.sleep(delayTime)
        time.sleep(audioToTextDelay)
        text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements(By.TAG_NAME,'span')
        result = " ".join( [ each.text for each in text ] )
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return result
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return "Error"
def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)
# def sbmit_click():
#     time.sleep(2)
#     driver.find_element(By.XPATH,'//button[@class = "submit" and text() = "Submit"]/ancestor::div[1]').click()
#     time.sleep(4)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.get(byPassUrl)
time.sleep(1)
googleClass = driver.find_elements(By.CLASS_NAME,'g-recaptcha')[0]
time.sleep(2)
outeriframe = googleClass.find_element(By.TAG_NAME,'iframe')
time.sleep(1)
outeriframe.click()
time.sleep(2)
allIframesLen = driver.find_elements(By.TAG_NAME,'iframe')
time.sleep(1)
audioBtnFound = False
audioBtnIndex = -1
for index in range(len(allIframesLen)):
    driver.switch_to.default_content()
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioBtn = driver.find_element(By.ID,'recaptcha-audio-button') or driver.find_element(By.ID,'recaptcha-anchor')
        audioBtn.click()
        audioBtnFound = True
        audioBtnIndex = index
        break
    except Exception as e:
        pass
if audioBtnFound:
    try:
        while True:
            href = driver.find_element(By.ID,'audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response,filename)
            response = audioToText(os.getcwd() + '/' + filename)
            print(response)
            driver.switch_to.default_content()
            iframe = driver.find_elements(By.TAG_NAME,'iframe')[audioBtnIndex]
            driver.switch_to.frame(iframe)
            inputbtn = driver.find_element(By.ID,'audio-response')
            inputbtn.send_keys(response)
            inputbtn.send_keys(Keys.ENTER)
            time.sleep(2)
            errorMsg = driver.find_elements(By.CLASS_NAME,'rc-audiochallenge-error-message')[0]
            if errorMsg.text == "" or errorMsg.value_of_css_property('display') == 'none':
                time.sleep(2)
                print("Success")
                driver.switch_to.default_content()
                driver.find_element(By.XPATH,'//button[@class = "submit" and text() = "Submit"]/ancestor::div[1]').click()
                time.sleep(2)
                break
    except Exception as e:
        print(e)
        print('Caught. Need to change proxy now')
        time.sleep(1)
else:
    time.sleep(1)
    print('Button not found. This should not happen.')
    time.sleep(1)


