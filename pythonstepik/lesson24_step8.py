import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

browser.get(link)

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

browser.find_element_by_id("book").click()

val = browser.find_element_by_id("input_value")
val_text = val.text

answer = calc(val_text)

browser.find_element_by_id("answer").send_keys(answer)
browser.find_element_by_id("solve").click()

answer_val = (browser.switch_to.alert.text).split(': ')[-1]
print(answer_val)

browser.quit()


