from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import USERNAME, PASSWORD

browser = webdriver.Safari()

browser.get("https://github.com/login")

login_field = browser.find_element(By.NAME, 'login')
login_field.send_keys(USERNAME)

password_field = browser.find_element(By.NAME, 'password')
password_field.send_keys(PASSWORD)

login_field.submit()

time.sleep(5)  
browser.quit()