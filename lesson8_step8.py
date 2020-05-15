from selenium import webdriver
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    input1.send_keys("Smolensk")
    input2 = browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    input2.send_keys("Smolensk")
    input3 = browser.find_element_by_css_selector("input[placeholder='Enter email']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("input[accept='.txt']")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()