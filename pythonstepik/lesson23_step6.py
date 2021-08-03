from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"

browser.get(link)

button = browser.find_element_by_css_selector('button[type = "submit"]')
button.click()

time.sleep(3)

new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

input_val = browser.find_element_by_id("input_value")
val = input_val.text
iv = calc(val)

inp = browser.find_element_by_id("answer").send_keys(iv)

browser.find_element_by_css_selector('button[type="submit"]').click()

answer_val = (browser.switch_to.alert.text).split(': ')[-1]
print(answer_val)

browser.quit()
