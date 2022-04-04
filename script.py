from typing import final
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import logging
logging.basicConfig(filename='example.log', format=' %(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
load_dotenv()

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Firefox()
driver.get("https://myaccount.sdge.com/portal/PreLogin/Validate")
try:
    wait0 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "usernamex"))
    )
finally: 
    print("wait0 found")
userNameField = driver.find_element(By.ID, "usernamex")
userNameField.send_keys(os.getenv('SDGE_USERNAME'))
userPassWord = driver.find_element(By.ID,"passwordx")
userPassWord.send_keys(os.getenv('SDGE_PASSWORD'))

try:
    wait1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID,"btnlogin"))
    )
finally:
    print("wait1 found")
    logging.info("wait1 found")
secondLogin = driver.find_element(By.ID,"btnlogin")
secondLogin.click()
driver.implicitly_wait(5)
try:
    wait2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Usage"))
    )
finally:
    print("wait2 found")
    logging.info("wait2 found")
hidePreloader = "document.getElementById('preloader').style.display = 'none';"
driver.execute_script(hidePreloader)
usageLink = driver.find_element(By.LINK_TEXT, "Usage")
usageLink.click()
driver.implicitly_wait(20)
hidePreloader = "document.getElementById('preloader').style.display = 'none';"
driver.execute_script(hidePreloader)
greenButtonDownload = driver.find_element(By.ID,"gbloadpopup")
webdriver.ActionChains(driver).move_to_element(greenButtonDownload).perform()
try:
    wait3 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID,"gbloadpopup"))
    )
finally:
    print("wait3 found")
    logging.info("wait3 found")
greenButtonDownload.click()
driver.switch_to.active_element
downloadScript = "document.getElementById('btngbDataDownload').click();"
driver.execute_script(downloadScript)
hidePreloader = "document.getElementById('preloader').style.display = 'none';"
driver.execute_script(hidePreloader)

driver.implicitly_wait(20)
downloadButton = driver.find_element(By.ID,"btngbDataDownload")
webdriver.ActionChains(driver).move_to_element(downloadButton).perform()
try:
    wait4 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID,"btngbDataDownload"))
    )
finally:
    print("wait4 found")
    logging.info("wait4 found")
downloadButton.click()
driver.implicitly_wait(20)

driver.quit()
