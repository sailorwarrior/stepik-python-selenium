from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/alert_accept.html"

browser.get(link)

button = browser.find_element_by_css_selector('button[type = "submit"]')
button.click()

confirm = browser.switch_to.alert
confirm.accept()

input_val = browser.find_element_by_id("input_value")
val = input_val.text
iv = calc(val)

inp = browser.find_element_by_id("answer").send_keys(iv)

browser.find_element_by_css_selector('button[type="submit"]').click()

answer_val = (browser.switch_to.alert.text).split(': ')[-1]
print(answer_val)

browser.quit()
