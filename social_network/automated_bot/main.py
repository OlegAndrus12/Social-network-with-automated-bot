import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DIR = os.getcwd()

driver = webdriver.Chrome(executable_path=DIR + "/automated_bot/chromedriver_linux64/chromedriver")

driver.maximize_window()
driver.get("http://127.0.0.1:8000/")

time.sleep(3)

driver.find_element_by_name("login_btn").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_name("username").send_keys("admin")
time.sleep(2)
driver.find_element_by_name("password").send_keys("admin")
time.sleep(2)
driver.find_element_by_name("login_btn").send_keys(Keys.ENTER)
#driver.close()