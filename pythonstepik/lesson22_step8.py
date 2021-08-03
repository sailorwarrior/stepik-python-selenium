import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

lastname_input = browser.find_element_by_css_selector('input[name="firstname"]')
firstname_input = browser.find_element_by_css_selector('input[name="lastname"]')
email_input = browser.find_element_by_css_selector('input[name="email"]')
upload_file = browser.find_element_by_id("file")

current_dir = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(current_dir, 'file.txt')

lastname_input.send_keys("Lastname")
firstname_input.send_keys("Firstname")
email_input.send_keys("email@mail.ru")
upload_file.send_keys(path)


browser.find_element_by_css_selector('button[type="submit"]').click()

time.sleep(30)
browser.quit()

