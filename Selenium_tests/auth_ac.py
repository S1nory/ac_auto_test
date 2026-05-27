from selenium import webdriver
from selenium.webdriver.common.by import By

import time
#import math


try: 
    
    link = "https://demo01.avroraos.ru/emm/admin/ui"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #input func
    #def calc(x):
    #    return str(math.log(abs(12*math.sin(int(x)))))
    
    
    #x_element = browser.find_element(By.ID, "login")
    #x = x_element.text
    val_login = "m.bautkin@omp.ru"
    val_password = "1qpg2242Y2***"


    #находим текстовое поле логин и вводим ответ
    input1 = browser.find_element(By.ID, "login")
    input1.send_keys(val_login)

    #находим текстовое поле пароль и вводим 
    input1 = browser.find_element(By.ID, "password")
    input1.send_keys(val_password)
    
    
    login_btn = browser.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')
    login_btn.click()


    #Ставим галочку о том что мы робот 
    #option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    #option1.click()
    
    #option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    #option2.click()

    #button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    #button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()