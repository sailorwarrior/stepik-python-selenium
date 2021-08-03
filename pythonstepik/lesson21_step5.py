from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(url)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(y)

radio = browser.find_element_by_id("robotCheckbox")
radio.click()

checkBox = browser.find_element_by_id("robotsRule")
checkBox.click()

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

browser.close()