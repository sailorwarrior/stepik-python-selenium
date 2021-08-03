from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

    n1 = int(num1.text)
    n2 = int(num2.text)

    result = n1 + n2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f"{result}")

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла