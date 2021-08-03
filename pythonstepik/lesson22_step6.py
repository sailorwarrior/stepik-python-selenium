from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"

browser.get(link)

input_val = browser.find_element_by_id("input_value")
val = input_val.text

count = calc(val)

input_answer = browser.find_element_by_id("answer").send_keys(count)

check = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()

radio = browser.find_element_by_id("robotsRule")
radio.click()

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

browser.