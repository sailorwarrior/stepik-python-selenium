from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    chest = browser.find_element_by_id("treasure")
    number = chest.get_attribute("valuex")

    y = calc(number)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    checkBox = browser.find_element_by_id("robotsRule")
    checkBox.click()
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()


finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла