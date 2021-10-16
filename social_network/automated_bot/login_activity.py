import time
from selenium.webdriver.common.keys import Keys

def login_user(driver, username, password):
    driver.find_element_by_name("login_btn").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_name("username").send_keys("admin")
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("admin")
    time.sleep(2)
    driver.find_element_by_name("login_btn").send_keys(Keys.ENTER)

def logout_user(driver):
    driver.find_element_by_name("logout_btn").send_keys(Keys.ENTER)

def register_user(driver, username, email, password):
    driver.find_element_by_name("register_btn").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_name("username").send_keys(username)
    time.sleep(2)
    driver.find_element_by_name("email").send_keys(email)
    time.sleep(2)
    driver.find_element_by_name("password1").send_keys(password)
    time.sleep(2)
    driver.find_element_by_name("password2").send_keys(password)
    time.sleep(2)
    driver.find_element_by_name("submit_btn").send_keys(Keys.ENTER)