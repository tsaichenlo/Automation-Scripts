from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import USERNAME, PASSWORD
import sys
import pyperclip


# login process
browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://github.com/login")

login_field = browser.find_element(By.NAME, 'login')
login_field.send_keys(USERNAME)

password_field = browser.find_element(By.NAME, 'password')
password_field.send_keys(PASSWORD)

login_field.submit()


# create new repo
try:
    repo_name = sys.argv[1]
except:
    print('Please provide repo name.')
    sys.exit()

try:
    visibility = sys.argv[2]
except:
    visibility = 'public'

browser.get('https://github.com/new')

name_field = browser.find_element(
    By.XPATH, '//input[@data-testid="repository-name-input"]')
name_field.send_keys(repo_name)

if visibility == 'private':
    visibility_field = browser.find_element(
        By.XPATH, '//input[@name="visibilityGroup" and @value="private"]')
else:
    visibility_field = browser.find_element(
        By.XPATH, '//input[@name="visibilityGroup" and @value="public"]')
visibility_field.click()

name_field.submit()

try:
    clipboard_button = browser.find_element(
        By.XPATH, '//clipboard-copy[@for="empty-setup-push-repo-echo"]')
    clipboard_button.click()

    print(pyperclip.paste())
except:
    print(f'Repository creation failed. Repo name must be unique')
