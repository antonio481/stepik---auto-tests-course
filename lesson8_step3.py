from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x = (int)(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = (int)(y_element.text)
    a=x+y
    a=str(a)
    browser.find_element_by_tag_name("select").click()
    input2=browser.find_element_by_id("dropdown")
    input2.send_keys(a)
    input3 = browser.find_element_by_class_name("btn.btn-default")
    input3.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()