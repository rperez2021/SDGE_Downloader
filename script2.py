from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
load_dotenv()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# For Debugging Only

# For Debugging Only

driver.get("https://myaccount.sdge.com/portal/PreLogin/Validate")
userNameField = driver.find_element(By.ID, "usernamex")
userNameField.send_keys(os.getenv('SDGE_USERNAME'))
driver.implicitly_wait(0.5)
userPassWord = driver.find_element(By.ID,"passwordx")
userPassWord.send_keys(os.getenv('SDGE_PASSWORD'))
driver.implicitly_wait(0.5)
secondLogin = driver.find_element(By.ID,"btnlogin")
secondLogin.click()
driver.implicitly_wait(10)
usageLink = driver.find_element_by_css_selector("#navbarSupportedContent > div > ul:nth-child(3) > li:nth-child(3) > a")
usageLink.click()
driver.implicitly_wait(10)
driver.switch_to.active_element
greenButtonDownload = driver.find_element(By.ID,"gbloadpopup")
greenButtonDownload.click()
driver.implicitly_wait(10)
driver.switch_to.active_element
downloadButton = driver.find_element(By.ID,"btngbDataDownload")
downloadButton.click()

# print(os.getenv('SDGE_USERNAME'))

# driver.quit()