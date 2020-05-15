from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input0=browser.find_element_by_id("answer")
    input0.send_keys(y)
    input1 = browser.find_element_by_id("robotCheckbox")
    input1.click()
    input2 = browser.find_element_by_id("robotsRule")
    input2.click()
    input3 = browser.find_element_by_class_name("btn.btn-default")
    input3.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()