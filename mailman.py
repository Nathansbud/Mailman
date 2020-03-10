from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import json

resource_path = os.path.join(os.path.dirname(__file__), "resources")
messenger_link = "https://www.messenger.com/t/"
with open(os.path.join(resource_path, "facebook.json")) as cf: creds = json.load(cf)
with open(os.path.join(resource_path, "people.json")) as pf: people = json.load(pf)



options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome(options=options)

browser.get(messenger_link+str(people['CS']))
browser.implicitly_wait(15)

browser.find_element_by_id("email").send_keys(creds['email'])
browser.find_element_by_id("pass").send_keys(creds['password'])
browser.find_element_by_id("loginbutton").click()

"""
Attempts to find message field:
    - .navigationFocus is parent div
    - div[@aria-label="Type a message..."] works for non-headless, but not with headless
    - .notranslate works; [-1] to account for group chat name (which also has notranslate)
"""
message_field = browser.find_elements_by_class_name("notranslate")[-1]
message_field.click()
message_field.send_keys("This is a test message sent from my command line; love y'all"+Keys.ENTER)

if __name__ == "__main__":
    pass