import os
import time
import utility
import json
import lorem
from random_username.generate import generate_username
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login_activity import login_user, logout_user, register_user
from post_activity import create_post, like_post_activity

DIR = os.getcwd()

driver = webdriver.Chrome(executable_path=DIR + "/chromedriver_linux64/chromedriver")
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")

with open('rules.json') as f:
    rules = json.load(f)
    f.close()


time.sleep(3)
login_user(driver, "admin", "admin")
time.sleep(3)
like_post_activity(driver)
logout_user(driver)
time.sleep(3)


for i in range(rules["number_of_users"]):
    mock_user = {
        "username" : generate_username(),
        "email" : utility.random_email_generator(),
        "password" : utility.generate_random_password(12),
    }
    register_user(driver, mock_user["username"], mock_user["email"], mock_user["password"])
    time.sleep(2)
    for j in range(rules["max_posts_per_user"]):
        create_post(driver)
        time.sleep(2)
    
    like_post_activity(driver, count_of_likes = rules["max_likes_per_user"])
    
    logout_user(driver)

driver.close()