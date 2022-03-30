import time
import lorem
from selenium.webdriver.common.keys import Keys


def create_post(driver):
    driver.find_element_by_name("create_post_btn").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_name("title").send_keys(lorem.sentence())
    time.sleep(2)
    driver.find_element_by_name("body").send_keys(lorem.paragraph())
    time.sleep(2)
    driver.find_element_by_name("create_btn").send_keys(Keys.ENTER)

def like_post_activity(driver, count_of_likes=1):
    not_liked_posts = list(filter(lambda x: not "dislike" in x.text, driver.find_elements_by_id("likin")))
    time.sleep(2)
    if len(not_liked_posts) == 0:
        print("No more posts to like")
    else:
        count_of_likes = len(not_liked_posts) if count_of_likes > len(not_liked_posts) else count_of_likes
        for i in range(count_of_likes):
            driver.find_element_by_partial_link_text("Click to like").click()
            time.sleep(2)
